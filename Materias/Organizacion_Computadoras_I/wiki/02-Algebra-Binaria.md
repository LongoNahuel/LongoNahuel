# Álgebra Binaria - Suma y Operaciones

## Tabla de Verdad de Suma Binaria (Sumador de 1 Bit)

| A | B | Cin | Suma (S) | Cout | Operación |
|---|---|-----|----------|------|-----------|
| 0 | 0 | 0   | 0        | 0    | 0 + 0 + 0 = 0 |
| 0 | 0 | 1   | 1        | 0    | 0 + 0 + 1 = 1 |
| 0 | 1 | 0   | 1        | 0    | 0 + 1 + 0 = 1 |
| 0 | 1 | 1   | 0        | 1    | 0 + 1 + 1 = 10₂ |
| 1 | 0 | 0   | 1        | 0    | 1 + 0 + 0 = 1 |
| 1 | 0 | 1   | 0        | 1    | 1 + 0 + 1 = 10₂ |
| 1 | 1 | 0   | 0        | 1    | 1 + 1 + 0 = 10₂ |
| 1 | 1 | 1   | 1        | 1    | 1 + 1 + 1 = 11₂ |

**Regla**: Si (A + B + Cin) ≥ 2 → Cout = 1

## Suma Binaria Paso a Paso

### Conceptos Clave

- **Acarreo de Entrada (Cin)**: Acarreo que entra desde la posición anterior
- **Acarreo de Salida (Cout)**: Acarreo que sale hacia la siguiente posición
- **BmS (Bit menos Significativo)**: Bit más a la derecha (donde comienza la suma)
- **BMS (Bit Más Significativo)**: Bit más a la izquierda (donde termina la suma)

### Ejemplo: 5 + 3 en 4 bits

```
Posición:    4  3  2  1
Acarreos:    ¹¹¹
A (5):       0  1  0  1
B (3):     + 0  0  1  1
          ─────────────
Y (8):       1  0  0  0

Cin_BMS = 1, Cout_BMS = 0
```

## Propagación de Carries en Sumador de 4 Bits

```
        B₃  A₃       B₂  A₂       B₁  A₁       B₀  A₀
         │   │        │   │        │   │        │   │
         └───┴──┐  ┌──┴───┴─┐  ┌──┴───┴─┐  ┌──┴───┴─┐
              C₃│  │C₂      │  │C₁      │  │C₀      │
            ┌───┘  │        │  │        │  │        │
            │    ┌─┴─┐    ┌─┴─┐      ┌─┴─┐      ┌─┴─┐
            │    │FA │◄───│FA │◄─────│FA │◄─────│FA │  (Sumador 4 bits)
            │    └─┬─┘    └─┬─┘      └─┬─┘      └─┬─┘
            │      │        │          │          │
            │      S₃       S₂         S₁         S₀ (Salidas)
            │
            └──────────────────────────────────────►
                      Propagación de Carry
                      (de derecha a izquierda)
```

## Próxima Sección

→ [[03-Punto-Fijo|Notación Q - Punto Fijo]]
