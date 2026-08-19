# Ejercicios Resueltos

## Ejercicio 1: Conversión Binario → Decimal

**Enunciado:** Convertir $(11010)_2$ a decimal.

**Solución aplicando el Teorema Fundamental con $B = 2$:**

$$A = \sum_{i=-m}^{n-1} A_i \cdot 2^i$$

Desglosado paso a paso:
$$(11010)_2 = 1 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot 2^0$$

Calculando cada término:
$$(11010)_2 = 1 \cdot 16 + 1 \cdot 8 + 0 \cdot 4 + 1 \cdot 2 + 0 \cdot 1$$

Sumando:
$$(11010)_2 = 16 + 8 + 0 + 2 + 0 = (26)_{10}$$

**Respuesta:** $(11010)_2 = (26)_{10}$ ✓

---

## Ejercicio 2: Conversión Hexadecimal → Decimal

**Enunciado:** Convertir $(2F5)_{16}$ a decimal.

**Solución aplicando el Teorema Fundamental con $B = 16$:**

Recordar: F = 15

$$(2F5)_{16} = 2 \cdot 16^2 + 15 \cdot 16^1 + 5 \cdot 16^0$$

Calculando:
$$(2F5)_{16} = 2 \cdot 256 + 15 \cdot 16 + 5 \cdot 1$$

$$(2F5)_{16} = 512 + 240 + 5 = (757)_{10}$$

**Respuesta:** $(2F5)_{16} = (757)_{10}$ ✓

---

## Ejercicio 3: Conversión Octal → Decimal

**Enunciado:** Convertir $(345)_8$ a decimal.

**Solución aplicando el Teorema Fundamental con $B = 8$:**

$$(345)_8 = 3 \cdot 8^2 + 4 \cdot 8^1 + 5 \cdot 8^0$$

Calculando:
$$(345)_8 = 3 \cdot 64 + 4 \cdot 8 + 5 \cdot 1$$

$$(345)_8 = 192 + 32 + 5 = (229)_{10}$$

**Respuesta:** $(345)_8 = (229)_{10}$ ✓

---

## Ejercicio 4: Conversión con Parte Fraccionaria (Binario)

**Enunciado:** Convertir $(101.101)_2$ a decimal.

**Solución:** Aplicar el Teorema Fundamental separando parte entera y fraccionaria.

**Parte entera:** $1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 = 4 + 0 + 1 = 5$

**Parte fraccionaria:** $1 \cdot 2^{-1} + 0 \cdot 2^{-2} + 1 \cdot 2^{-3} = 0.5 + 0 + 0.125 = 0.625$

$$(101.101)_2 = 5 + 0.625 = (5.625)_{10}$$

**Respuesta:** $(101.101)_2 = (5.625)_{10}$ ✓

---

## Ejercicio 5: Identificar Base de un Número

**Enunciado:** Si un número se escribe como $(120)_B$ y su equivalente en decimal es $(15)_{10}$, ¿cuál es la base $B$?

**Solución:** Aplicar el Teorema Fundamental:

$$(120)_B = 1 \cdot B^2 + 2 \cdot B^1 + 0 \cdot B^0 = 15$$

$$B^2 + 2B = 15$$

$$B^2 + 2B - 15 = 0$$

Factorizando: $(B + 5)(B - 3) = 0$

Como $B > 0$ y debe ser mayor que 2 (el dígito de mayor valor que aparece): $B = 3$

**Verificación:** $(120)_3 = 1 \cdot 3^2 + 2 \cdot 3^1 + 0 \cdot 3^0 = 9 + 6 + 0 = (15)_{10}$ ✓

**Respuesta:** $B = 3$ (Sistema Ternario) ✓
