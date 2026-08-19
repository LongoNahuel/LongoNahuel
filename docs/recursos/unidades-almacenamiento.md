# Unidades de Almacenamiento Binario

Tabla completa de unidades de almacenamiento digital basadas en potencias de 2.

## Jerarquía de Unidades Binarias

Las unidades de almacenamiento en sistemas informáticos se basan en potencias de 2.

| Unidad | Símbolo | Definición | En Bytes | En Binario |
|--------|---------|-----------|----------|-----------|
| **Bit** | b | Unidad mínima (0 o 1) | $2^{-3}$ (0.125) | $2^0$ |
| **Byte** | B | 8 bits | $2^0$ | $2^3$ bits |
| **Kilobyte Binario** | KiB | $2^{10}$ bytes | $2^{10}$ | $2^{10}$ bytes |
| **Megabyte Binario** | MiB | $2^{10}$ KiB | $2^{20}$ | $2^{20}$ bytes |
| **Gigabyte Binario** | GiB | $2^{10}$ MiB | $2^{30}$ | $2^{30}$ bytes |
| **Terabyte Binario** | TiB | $2^{10}$ GiB | $2^{40}$ | $2^{40}$ bytes |
| **Petabyte Binario** | PiB | $2^{10}$ TiB | $2^{50}$ | $2^{50}$ bytes |
| **Exabyte Binario** | EiB | $2^{10}$ PiB | $2^{60}$ | $2^{60}$ bytes |
| **Zettabyte Binario** | ZiB | $2^{10}$ EiB | $2^{70}$ | $2^{70}$ bytes |
| **Yottabyte Binario** | YiB | $2^{10}$ ZiB | $2^{80}$ | $2^{80}$ bytes |

## Equivalencias en Bytes

### Unidades Pequeñas

| Unidad | Bytes | Cálculo |
|--------|-------|---------|
| 1 Bit | 0.125 | $2^{-3}$ |
| 1 Byte | 1 | $2^0$ |
| 1 Kilobyte Binario (KiB) | 1,024 | $2^{10}$ |
| 1 Megabyte Binario (MiB) | 1,048,576 | $2^{20}$ |
| 1 Gigabyte Binario (GiB) | 1,073,741,824 | $2^{30}$ |

### Unidades Grandes

| Unidad | Bytes | Notación Científica |
|--------|-------|-------------------|
| 1 Terabyte Binario (TiB) | $2^{40}$ | $1.0995... \times 10^{12}$ |
| 1 Petabyte Binario (PiB) | $2^{50}$ | $1.1259... \times 10^{15}$ |
| 1 Exabyte Binario (EiB) | $2^{60}$ | $1.1529... \times 10^{18}$ |
| 1 Zettabyte Binario (ZiB) | $2^{70}$ | $1.1806... \times 10^{21}$ |
| 1 Yottabyte Binario (YiB) | $2^{80}$ | $1.2089... \times 10^{24}$ |

## Tabla de Potencias de 2

Referencia rápida de exponentes para unidades de almacenamiento.

| Exponente | $2^n$ | Unidad | Equivalencia |
|-----------|-------|--------|--------------|
| $2^0$ | 1 | — | 1 Byte |
| $2^3$ | 8 | — | 1 Byte = 8 bits |
| $2^{10}$ | 1,024 | KiB | Kilobyte Binario |
| $2^{20}$ | 1,048,576 | MiB | Megabyte Binario |
| $2^{30}$ | 1,073,741,824 | GiB | Gigabyte Binario |
| $2^{40}$ | 1,099,511,627,776 | TiB | Terabyte Binario |
| $2^{50}$ | 1,125,899,906,842,624 | PiB | Petabyte Binario |
| $2^{60}$ | 1,152,921,504,606,846,976 | EiB | Exabyte Binario |
| $2^{70}$ | 1,180,591,620,717,411,303,424 | ZiB | Zettabyte Binario |
| $2^{80}$ | 1,208,925,819,614,629,174,706,176 | YiB | Yottabyte Binario |

## Contexto Histórico: KiB vs KB

**Importante:** Existe diferencia entre:

- **KiB (Kilobyte Binario):** $2^{10}$ = 1,024 bytes (estándar en computadoras)
- **KB (Kilobyte Decimal):** $10^3$ = 1,000 bytes (estándar comercial/marketing)

La confusión surge porque en los primeros tiempos, "KB" se usaba para ambos. Actualmente:
- **IEC (International Electrotechnical Commission)** recomienda: KiB, MiB, GiB, etc. para binario
- **ISO/SI (International System of Units)** mantiene: KB, MB, GB, etc. para decimal

### Ejemplo de Diferencia

**1 Gigabyte (decimal vs binario):**

- $(1,000,000,000)_{10}$ bytes (decimal) = 1 GB
- $(1,073,741,824)_{10}$ bytes (binario) = 1 GiB

**Diferencia:** Aproximadamente 73 MB de más en la versión binaria

## Aplicaciones Prácticas

### En Sistemas de Archivos

La mayoría de sistemas de archivos modernos (ext4, NTFS, APFS) reportan tamaños en **unidades binarias (GiB, TiB)**, aunque muchas aplicaciones los muestran como "GB", "TB".

### En Memoria RAM

La RAM siempre se expresa en **potencias de 2:**
- 1 GB RAM = $2^{30}$ bytes (no $10^9$ bytes)
- 8 GB RAM = $8 \times 2^{30}$ bytes

### En Almacenamiento en Nube

Los proveedores a menudo utilizan **decimales (GB)** en marketing, pero la capacidad real es **binaria (GiB)**.

## Conversiones Comunes

### De Bytes a Otras Unidades

Para convertir bytes a KiB: Dividir por $2^{10}$ (1,024)
```
1,048,576 bytes ÷ 1,024 = 1,024 KiB = 1 MiB
```

Para convertir bytes a GiB: Dividir por $2^{30}$ (1,073,741,824)
```
1,073,741,824 bytes ÷ 1,073,741,824 = 1 GiB
```

### Conversiones Inversas

Para convertir KiB a bytes: Multiplicar por $2^{10}$ (1,024)
```
100 KiB × 1,024 = 102,400 bytes
```

Para convertir GiB a MiB: Multiplicar por $2^{10}$ (1,024)
```
2 GiB × 1,024 = 2,048 MiB
```

## Fórmula General

Para cualquier unidad binaria de almacenamiento con exponente $n$:

$$\text{Bytes} = \text{Cantidad} \times 2^n$$

**Ejemplo:** Si tienes 5 GiB (n=30):
$$\text{Bytes} = 5 \times 2^{30} = 5 \times 1,073,741,824 = 5,368,709,120 \text{ bytes}$$
