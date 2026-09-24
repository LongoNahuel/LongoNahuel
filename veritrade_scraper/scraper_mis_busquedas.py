"""
Scraper de "Mis búsquedas" en Veritrade Business.

La página requiere login, así que el script abre un navegador real (Chromium via
Playwright) con un perfil persistente: la primera vez iniciás sesión a mano y
las siguientes ejecuciones reutilizan la sesión guardada.

Extrae todas las tablas visibles (<table> HTML y grillas tipo role="grid") y las
guarda en un Excel (una hoja por tabla) y en CSVs.

Uso:
    pip install playwright pandas openpyxl lxml
    playwright install chromium
    python scraper_mis_busquedas.py
"""

from datetime import datetime
from io import StringIO
from pathlib import Path

import pandas as pd
from playwright.sync_api import sync_playwright

URL = "https://business2.veritradecorp.com/es/mis-busquedas"
BASE_DIR = Path(__file__).resolve().parent
PERFIL_DIR = BASE_DIR / ".perfil_navegador"  # guarda cookies/sesión
SALIDA_DIR = BASE_DIR / "salida"


def esperar_login(page):
    """Si Veritrade redirige al login, espera a que el usuario inicie sesión."""
    if "mis-busquedas" in page.url:
        return
    print("\n>> Iniciá sesión en la ventana del navegador.")
    input(">> Cuando veas la página 'Mis búsquedas', presioná ENTER acá... ")
    if "mis-busquedas" not in page.url:
        page.goto(URL, wait_until="networkidle")


def extraer_tablas_html(page):
    """Lee todos los <table> del DOM (incluidos iframes) con pandas."""
    tablas = []
    for frame in page.frames:
        try:
            html = frame.content()
        except Exception:
            continue
        if "<table" not in html.lower():
            continue
        try:
            tablas.extend(pd.read_html(StringIO(html)))
        except ValueError:
            pass  # no había tablas parseables
    # descartar tablas vacías o de maquetación (1 sola celda)
    return [t for t in tablas if t.shape[0] > 0 and t.shape[1] > 1]


def extraer_grillas_div(page):
    """Extrae grillas armadas con <div role="grid"/"row"/"cell"> (Angular/React)."""
    datos = page.evaluate(
        """
        () => [...document.querySelectorAll('[role="grid"], [role="table"]')]
          .filter(g => g.tagName !== 'TABLE')
          .map(g => [...g.querySelectorAll('[role="row"]')].map(r =>
              [...r.querySelectorAll(
                  '[role="columnheader"], [role="cell"], [role="gridcell"]'
              )].map(c => c.innerText.trim())
          ).filter(r => r.length))
        """
    )
    tablas = []
    for filas in datos:
        if len(filas) < 2:
            continue
        encabezado, cuerpo = filas[0], filas[1:]
        ancho = max(len(f) for f in filas)
        encabezado = encabezado + [f"col_{i}" for i in range(len(encabezado), ancho)]
        cuerpo = [f + [""] * (ancho - len(f)) for f in cuerpo]
        tablas.append(pd.DataFrame(cuerpo, columns=encabezado))
    return tablas


def guardar(tablas):
    SALIDA_DIR.mkdir(exist_ok=True)
    sello = datetime.now().strftime("%Y%m%d_%H%M%S")
    excel = SALIDA_DIR / f"mis_busquedas_{sello}.xlsx"
    with pd.ExcelWriter(excel, engine="openpyxl") as writer:
        for i, df in enumerate(tablas, 1):
            df.to_excel(writer, sheet_name=f"tabla_{i}", index=False)
            df.to_csv(SALIDA_DIR / f"mis_busquedas_{sello}_tabla_{i}.csv",
                      index=False, encoding="utf-8-sig")
    return excel


def main():
    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            str(PERFIL_DIR), headless=False, viewport={"width": 1400, "height": 900}
        )
        page = ctx.pages[0] if ctx.pages else ctx.new_page()
        page.goto(URL, wait_until="networkidle")
        esperar_login(page)

        # dar tiempo a que la SPA cargue la grilla
        page.wait_for_timeout(3000)
        page.screenshot(path=str(BASE_DIR / "captura_mis_busquedas.png"), full_page=True)

        tablas = extraer_tablas_html(page) + extraer_grillas_div(page)
        if not tablas:
            print("No se encontraron tablas. Revisá captura_mis_busquedas.png")
            (BASE_DIR / "pagina_debug.html").write_text(page.content(), encoding="utf-8")
        else:
            for i, df in enumerate(tablas, 1):
                print(f"\n=== Tabla {i}: {df.shape[0]} filas x {df.shape[1]} columnas ===")
                print(df.head(10).to_string(index=False))
            print(f"\nGuardado en: {guardar(tablas)}")

        ctx.close()


if __name__ == "__main__":
    main()
