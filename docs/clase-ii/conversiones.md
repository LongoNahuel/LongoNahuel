# Métodos de Conversión

## Conversión Base B → Decimal (Base 10)

Utilizamos el **Teorema Fundamental de la Enumeración** como método universal.

### Método: Aplicar Teorema Fundamental

$$N = \sum_{i=-m}^{n-1} A_i \cdot B^i$$

**Pasos:**
1. Identificar la base B del número
2. Asignar índices de posición: posición 0 es el dígito más a la derecha de la parte entera
3. Multiplicar cada dígito por B elevado a su índice
4. Sumar todos los términos

### Ejemplo: Binario a Decimal

Convertir $(1101)_2$ a decimal:

$$(1101)_2 = 1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0$$
$$= 1 \cdot 8 + 1 \cdot 4 + 0 \cdot 2 + 1 \cdot 1$$
$$= 8 + 4 + 0 + 1 = (13)_{10}$$

## Conversión Decimal → Base B

### Método: División Sucesiva (Parte Entera)

**Pasos:**
1. Dividir el número entre la base B
2. Anotar el resto
3. Dividir el cociente entre B nuevamente
4. Repetir hasta que el cociente sea 0
5. Leer los restos de **abajo hacia arriba**

### Ejemplo: Decimal a Binario

Convertir $(26)_{10}$ a binario:

```
26 ÷ 2 = 13 resto 0
13 ÷ 2 = 6  resto 1
6  ÷ 2 = 3  resto 0
3  ÷ 2 = 1  resto 1
1  ÷ 2 = 0  resto 1
```

Leyendo de abajo hacia arriba: $(26)_{10} = (11010)_2$

**Verificación:** $1 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot 2^0 = 16 + 8 + 2 = 26$ ✓

### Método: Multiplicación Sucesiva (Parte Fraccionaria)

Para convertir fracciones decimales a otra base:

**Pasos:**
1. Multiplicar la fracción por la base B
2. Anotar la parte entera del resultado
3. Usar la parte fraccionaria para el siguiente paso
4. Repetir hasta obtener la precisión deseada (o fracción = 0)

### Ejemplo: Decimal Fraccionario a Binario

Convertir $(0.625)_{10}$ a binario:

```
0.625 × 2 = 1.25    → dígito: 1
0.25  × 2 = 0.5     → dígito: 0
0.5   × 2 = 1.0     → dígito: 1
```

Leyendo de arriba hacia abajo: $(0.625)_{10} = (0.101)_2$

## Conversiones Rápidas (Pasajes Directos)

### Binario ↔ Octal

Cada dígito octal equivale a 3 dígitos binarios.

**Agrupación: 3 dígitos binarios → 1 dígito octal**

Ejemplo: $(110101)_2 \rightarrow (110)(101)_2 = (6)(5)_8 = (65)_8$

### Binario ↔ Hexadecimal

Cada dígito hexadecimal equivale a 4 dígitos binarios.

**Agrupación: 4 dígitos binarios → 1 dígito hexadecimal**

Ejemplo: $(11010101)_2 \rightarrow (1101)(0101)_2 = (D)(5)_{16} = (D5)_{16}$

### Octal ↔ Hexadecimal

**Método:** Convertir a binario como intermediario.

1. Octal → Binario (expandir cada dígito a 3 bits)
2. Binario → Hexadecimal (agrupar en 4 bits)

Ejemplo: $(175)_8 = (001)(111)(101)_2 = (0011)(1110)(1)_2 = (0011)(1110)(0001)_2 = (3E1)_{16}$

## Selección del Método Apropiado

| Conversión | Método Recomendado |
|------------|-------------------|
| Cualquier Base → Decimal | Teorema Fundamental |
| Decimal → Cualquier Base | División sucesiva (entero) + Multiplicación sucesiva (fracción) |
| Binario ↔ Octal | Agrupación directa (3 bits) |
| Binario ↔ Hexadecimal | Agrupación directa (4 bits) |
| Octal ↔ Hexadecimal | A través de Binario |

## Estrategia General

1. **Si necesitas cualquier base → Decimal:** Usa Teorema Fundamental
2. **Si necesitas Decimal → cualquier base:** Usa división/multiplicación sucesiva
3. **Si necesitas conversiones entre Binario, Octal, Hexadecimal:** Usa pasajes rápidos (agrupación)
