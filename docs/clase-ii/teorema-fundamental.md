# Teorema Fundamental de la Enumeración

## Fórmula General

**Fórmula general** para convertir un número en cualquier base B a base 10 (decimal):

$$N = \sum_{i=-m}^{n-1} A_i \cdot B^i$$

**Expandido:**
$$N = A_{n-1} \cdot B^{n-1} + \ldots + A_1 \cdot B^1 + A_0 \cdot B^0 + A_{-1} \cdot B^{-1} + \ldots + A_{-m} \cdot B^{-m}$$

## Significado de las Variables

- $N$ = número en decimal
- $\sum$ = sumatoria (suma acumulativa)
- $i$ = índice de posición (desde $-m$ hasta $n-1$)
- $A_i$ = dígito/símbolo en posición $i$
- $B$ = base del sistema numérico
- $n$ = cantidad de dígitos en la parte entera
- $m$ = cantidad de dígitos en la parte fraccionaria

## Partes del Número

- **La parte entera** se calcula de los exponentes positivos (0, 1, 2, ...)
- **La parte fraccionaria** se calcula de los exponentes negativos (-1, -2, -3, ...)

## Concepto Clave

**El Teorema Fundamental NO cambia.** Solo cambia el valor de $B$ según el sistema:

- Si $B = 2$ → Conversión **Binario → Decimal**
- Si $B = 8$ → Conversión **Octal → Decimal**
- Si $B = 16$ → Conversión **Hexadecimal → Decimal**
- Si $B = 5$ → Conversión **Base-5 → Decimal**

## Ejemplos de Aplicación

### Binario (B=2)
$$(11010)_2 = 1 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot 2^0 = 16 + 8 + 2 = (26)_{10}$$

### Hexadecimal (B=16)
$$(1A3)_{16} = 1 \cdot 16^2 + 10 \cdot 16^1 + 3 \cdot 16^0 = 256 + 160 + 3 = (419)_{10}$$

### Octal (B=8)
$$(175)_8 = 1 \cdot 8^2 + 7 \cdot 8^1 + 5 \cdot 8^0 = 64 + 56 + 5 = (125)_{10}$$

### Con Parte Fraccionaria
$$(101.101)_2 = 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 + 1 \cdot 2^{-1} + 0 \cdot 2^{-2} + 1 \cdot 2^{-3}$$
$$= 4 + 1 + 0.5 + 0.125 = (5.625)_{10}$$

## Por Qué es Fundamental

1. **Universalidad:** Funciona para cualquier base
2. **Simplicidad:** Una sola fórmula para todas las conversiones
3. **Poder:** Permite identificar bases desconocidas
4. **Elegancia Matemática:** Demuestra la uniformidad de los sistemas numéricos

## Metáfora Pedagógica

Es como si el Teorema fuera una **máquina universal** que acepta cualquier base como entrada:
- Pones Base 2 → Convierte de binario
- Pones Base 8 → Convierte de octal
- Pones Base 16 → Convierte de hexadecimal
- Pones Base 5 → Convierte de base 5

La máquina sigue el mismo proceso, solo el parámetro B cambia.
