# Sistemas Numéricos

## Sistemas de Notación Posicional (SNP)

Un sistema de notación posicional tiene:
- Un conjunto de **N símbolos** (Ej: 0–9 en decimal)
- Una **posición** que determina el peso/valor de cada símbolo
- Los símbolos se organizan dentro de una cadena para representar el número

La posición del símbolo define su valor multiplicado por potencias de la base del sistema.

## Sistemas Principales

### Sistema Decimal (Base 10, B=10)

Utiliza 10 símbolos: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

$$N = \sum_{i=-m}^{n-1} d_i \cdot 10^i$$

**Ejemplo:** $345.67 = 3 \cdot 10^2 + 4 \cdot 10^1 + 5 \cdot 10^0 + 6 \cdot 10^{-1} + 7 \cdot 10^{-2}$

### Sistema Binario (Base 2, B=2)

Utiliza 2 símbolos: {0, 1}

$$N = \sum_{i=-m}^{n-1} b_i \cdot 2^i$$

**Ejemplo:** $(1011)_2 = 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0 = (11)_{10}$

**Nota importante:** LA BASE VA A SER SIEMPRE 2

### Sistema Octal (Base 8, B=8)

Utiliza 8 símbolos: {0, 1, 2, 3, 4, 5, 6, 7}

$$N = \sum_{i=-m}^{n-1} o_i \cdot 8^i$$

**Ejemplo:** $(75)_8 = 7 \cdot 8^1 + 5 \cdot 8^0 = 56 + 5 = (61)_{10}$

**Aplicación:** Común en sistemas UNIX/Linux para permisos de archivos (rwx = octal).

### Sistema Hexadecimal (Base 16, B=16)

Utiliza 16 símbolos: {0–9, A–F} donde A=10, B=11, ..., F=15

$$N = \sum_{i=-m}^{n-1} h_i \cdot 16^i$$

**Ejemplo:** $(1A3)_{16} = 1 \cdot 16^2 + 10 \cdot 16^1 + 3 \cdot 16^0 = 419_{10}$

**Nota importante:** Solo en este sistema se debe tener en cuenta a qué equivale cada letra para aplicar la fórmula genérica.

### Sistema Base 64

Símbolos: {0–9, a–z, A–Z, +, /}

**Aplicación práctica:** Se utiliza en Oracle con el atributo `ROWID` para identificar de forma única cada elemento en la base de datos.

## Comparativa de Sistemas

| SRN | Base (B) | Símbolos |
|-----|----------|----------|
| **Binario** | 2 | {0, 1} |
| **Octal** | 8 | {0, 1, 2, 3, 4, 5, 6, 7} |
| **Decimal** | 10 | {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} |
| **Hexadecimal** | 16 | {0-9, A-F} |

## Conceptos Fundamentales

### Base (B)
Es la cantidad de símbolos diferentes que utiliza el sistema. Define cuántos valores distintos puede representar cada posición.

### Símbolos
Conjunto finito de caracteres usados para escribir números en el sistema. El número de símbolos es igual a la base.

### Peso de Posición
Cada posición tiene un peso que es una potencia de la base. El peso aumenta de derecha a izquierda (de menor a mayor potencia).

### Cantidad de Símbolos por Base
- En base 2: 2 símbolos
- En base 8: 8 símbolos
- En base 10: 10 símbolos
- En base 16: 16 símbolos (incluye letras A–F)

## Características Generales de todo Sistema Numérico

1. **Posicionalidad:** El valor de un símbolo depende de su posición en la cadena
2. **Base definida:** Cada sistema tiene una base específica que determina cuántos símbolos usa
3. **Notación uniforme:** Todos siguen el Teorema Fundamental de la Enumeración
4. **Versatilidad:** Permite representar números enteros y fraccionarios
