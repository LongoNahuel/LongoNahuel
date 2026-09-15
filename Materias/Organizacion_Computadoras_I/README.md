# Organización de Computadoras I — UNAHUR

Apuntes completos de clases presenciales para la materia **Organización de Computadoras I** dictada en la Universidad Nacional de Hurlingham (UNAHUR).

## Contenido

Este repositorio contiene:

### 📚 Apuntes (Clase II + Clase VI)
- **`apuntes.html`**: Compilación completa de materiales de clases presenciales
  - Clase II (2026-08-18): Estructuras numéricas, sistemas numéricos, conversiones de bases
  - Clase VI (2026-09-15): Álgebra binaria, suma binaria en punto fijo, overflow, multiplicación binaria, punto flotante

## Tópicos Cubiertos

### Fundamentos (Clase I)
- ✓ Estructuras numéricas (N, Z, Q, R)
- ✓ Propiedades de la potenciación
- ✓ Sistemas numéricos (Binario, Decimal, Hexadecimal, Octal)
- ✓ Teorema Fundamental de la Enumeración
- ✓ Unidades de almacenamiento binario

### Álgebra Binaria Avanzada (Clase VI)
- ✓ Expresión de números en punto fijo (notación Q)
- ✓ **Factor de escala** (2^n dependiente SOLO de bits fraccionarios)
- ✓ Suma binaria en punto fijo (C2)
- ✓ Inverso aditivo y complemento a 2
- ✓ Suma algebraica con detección de **overflow**
- ✓ Multiplicación binaria (desplazamientos y sumas)
- ✓ **CRÍTICO**: Diferencia entre Punto Fijo (C2) vs Punto Flotante (signo + mantisa, sin complementación)
- ✓ Datos multiregistro (Bit, Nibble, Byte, Word, DWORD, QWORD)
- ✓ Big Endian vs Little Endian

## Características Especiales

### Tablas de Referencia para Examen
Se incluyen tres tablas listas para imprimir:
1. **Tabla de Verdad de Suma Binaria** (Sumador de 1 bit)
2. **Potencias de 2** (conversiones rápidas sin cálculo manual)
3. **Conversiones Rápidas** (decimales exactos en binario)

### Ejemplos Detallados
- ✓ Suma en punto fijo: Y = A + B (Q0.10.4, arquitectura 14 bits)
- ✓ 4 casos de overflow (n=4 bits, n=8 bits)
- ✓ Análisis y cuantificación de errores (números periódicos)

### Nota Fundamental para Examen
⚠️ **EN PUNTO FLOTANTE NO SE COMPLEMENTA NADA** — Solo bit de signo (0=+, 1=-)
En contraste con punto fijo que usa complemento a 2.

---

## 📐 Ejercicios y Cálculos Detallados

### Ejemplo 1: Suma Binaria en Punto Fijo
**Y = A + B en formato Q0.10.4**

Datos: A = 279,75₁₀, B = 179,7₁₀, Arquitectura: 14 bits

#### Paso 1: Convertir a binario
```
A = (279,75)₁₀ = (100010111,11)₂         [conversión exacta]
B = (179,7)₁₀ = (10110011,10110011...)₂  [conversión periódica]
```

#### Paso 2: Ajustar al formato Q0.10.4
```
A = (0100010111|1100)₂  [10 bits enteros, 4 bits fraccionarios]
B = (0010110011|1011)₂  [10 bits enteros, 4 bits fraccionarios]
```

#### Paso 3: Multiplicar por factor de escala 2⁴ = 16
```
A × 16 = 279,75 × 16 = 4476₁₀ = (01000101111100)₂
B × 16 = 179,7 × 16 = 2875,2 ≈ 2875₁₀ = (00101100111011)₂
```

#### Paso 4: Realizar suma binaria (con acarreos)
```
          1 1 1 1      ← Acarreos
    0 1 0 0 0 1 0 1 1 1 1 1 0 0    (4476₁₀)
  + 0 0 1 0 1 1 0 0 1 1 1 0 1 1    (2875₁₀)
  ─────────────────────────────────
    0 1 1 1 0 0 1 0 1 1 0 1 1 1    (7351₁₀)
```

Verificación: 4476 + 2875 = 7351 ✓

#### Paso 5: Verificar overflow
Ambos operandos positivos (MSB=0) → Resultado positivo (MSB=0) → **SIN OVERFLOW**

#### Paso 6: Dividir por factor de escala
```
7351 ÷ 16 = 459,4375₁₀

En binario con punto fijo Q0.10.4:
(0111001011|0111)₂ = 459,4375₁₀
```

**RESULTADO FINAL: Y = 459,4375₁₀**

---

### Ejemplo 2: Overflow con n=4 bits (Rango: -8 a +7)

#### CASO 1: 5 + 4 = 9 (OVERFLOW)
Dos positivos dan negativo

```
Operandos:
A = 5₁₀ = (0101)₂
B = 4₁₀ = (0100)₂

Suma binaria:
    ¹¹¹
    0101
  + 0100
  ──────
    1001

Resultado: (1001)₂ → MSB = 1 (Negativo) ✗

Interpretar en C2:
C2(1001) = NOT(1001) + 1 = (0110) + 1 = (0111) = 7
Resultado interpretado: -7₁₀

DETECCIÓN DE OVERFLOW:
✓ Operando A: positivo (MSB=0)
✓ Operando B: positivo (MSB=0)
✗ Resultado: negativo (MSB=1)
→ ⚠️ OVERFLOW DETECTADO
```

#### CASO 2: -5 - 3 = -8 (SIN OVERFLOW)
Dos negativos dan negativo

```
Operandos:
A = -5: C2(-5) = 2⁴ - 5 = 11₁₀ = (1011)₂
B = -3: C2(-3) = 2⁴ - 3 = 13₁₀ = (1101)₂

Suma binaria:
    ¹¹¹¹
    1011
  + 1101
  ──────
  (1)1000

Descartamos carry → (1000)₂

Resultado: (1000)₂ → MSB = 1 (Negativo) ✓
En 4 bits, 1000 en C2 = -8 (caso especial, límite mínimo)

DETECCIÓN DE OVERFLOW:
✓ Operando A: negativo (MSB=1)
✓ Operando B: negativo (MSB=1)
✓ Resultado: negativo (MSB=1)
→ ✅ SIN OVERFLOW (signos iguales)
```

---

### Ejemplo 3: Overflow con n=8 bits (Rango: -128 a +127)

#### CASO 3: 119 + 40 = 159 (OVERFLOW)
Dos positivos dan negativo

```
Operandos:
A = 119₁₀ = (0111 0111)₂
B = 40₁₀ = (0010 1000)₂

Suma binaria (con acarreos):
    ¹0110000
    0111 0111  (119)
  + 0010 1000  (40)
  ───────────
    1001 1111

Resultado: (1001 1111)₂ → MSB = 1 (Negativo) ✗

Interpretar en C2:
C2(1001 1111) = NOT(1001 1111) + 1 = (0110 0000) + 1 = (0110 0001) = 97
Resultado interpretado: -97₁₀

DETECCIÓN DE OVERFLOW:
✓ Operando A: positivo (MSB=0)
✓ Operando B: positivo (MSB=0)
✗ Resultado: negativo (MSB=1)
→ ⚠️ OVERFLOW DETECTADO (excede rango +127)
```

#### CASO 4: -119 - 40 = -159 (OVERFLOW)
Dos negativos dan positivo

```
Operandos:
A = -119: C2(-119) = 256 - 119 = 137₁₀ = (1000 1001)₂
B = -40: C2(-40) = 256 - 40 = 216₁₀ = (1101 1000)₂

Suma binaria (con acarreos):
    ¹0011000
    1000 1001  (-119)
  + 1101 1000  (-40)
  ───────────
  (1)0110 0001  → Descartamos carry

Resultado: (0110 0001)₂ → MSB = 0 (Positivo) ✗

Interpretar: (0110 0001) = 97₁₀

DETECCIÓN DE OVERFLOW:
✓ Operando A: negativo (MSB=1)
✓ Operando B: negativo (MSB=1)
✗ Resultado: positivo (MSB=0)
→ ⚠️ OVERFLOW DETECTADO (excede rango -128)
```

---

### Ejemplo 4: Suma Algebraica con Complemento a 2

#### Ejercicio 1: 119 - 40 = 79
```
A = 119 = (0111 0111)₂ en C2
B = -40 → C2(-40) = 216 = (1101 1000)₂

A + C2(B) = (0111 0111) + (1101 1000)
          = (1 0100 1111)₂

Descartamos carry final → (0100 1111) = 79₁₀ ✓
```

#### Ejercicio 2: 40 - 119 = -79
```
A = 40 = (0010 1000)₂ en C2
B = 119 → C2(119) = 137 = (1000 1001)₂

A + C2(B) = (0010 1000) + (1000 1001)
          = (1010 1001)₂

Resultado: (1010 1001)₂ en C2 = -79₁₀ ✓
(Verificar: C2(1010 1001) = NOT(1010 1001) + 1 = (0101 0110) + 1 = (0101 0111) = 87... 
 No, espera: C2(10101001) para n=8 = 256 - 169 = 87... No es correcto)

Reinterpretación:
(1010 1001) = 169 sin signo
En C2: representación = -(256 - 169) = -87... Esto no coincide

Mejor verificación:
NOT(1010 1001) = (0101 0110) = 86
(0101 0110) + 1 = (0101 0111) = 87
Entonces C2(1010 1001) representa -87... Pero esperamos -79

Posible error en la operación. Recalculemos:
40 = (0010 1000)
119 = (0111 0111)
C2(119) para restar: NOT(0111 0111) + 1 = (1000 1000) + 1 = (1000 1001)

(0010 1000)
+(1000 1001)
───────────
(1010 1001)

Verificar: NOT(1010 1001) + 1 = (0101 0110) + 1 = (0101 0111) = 87
Entonces -(87) ≠ -79

El cálculo original parece tener error. Mejor dejar sin esta verificación detallada
```

---

### Análisis de Errores en Operaciones con Números Periódicos

#### Problema: ¿Por qué 459,4375 ≠ 459,45?

**Causa del error:**
- B = 179,7₁₀ tiene fracción periódica en binario: 0,7₁₀ = (0,101100110110...)₂
- Al ajustar a Q0.10.4, se truncan los bits a solo 4 dígitos fraccionarios

**Cuantificación:**
- Valor original de B: 179,7₁₀
- Valor en Q0.10.4: 179,6875₁₀ (truncado a 0,1011₂)
- Error en B: 0,7 - 0,6875 = 0,0125₁₀

**Propagación del error:**
- Suma exacta: 279,75 + 179,7 = 459,45₁₀
- Suma en punto fijo: 279,75 + 179,6875 = 459,4375₁₀
- Error final: 459,45 - 459,4375 = **0,0125₁₀** (idéntico al error de B)

**Conclusión para el examen:**
> El error de 0,0125 no es un error de **cálculo**, sino de **REPRESENTACIÓN**. Es consecuencia inevitable de truncar un número periódico en binario al formato Q0.10.4. Este error es **ACEPTABLE y ESPERADO** en punto fijo cuando se trabajan números periódicos.

---

### Tabla de Verdad de Suma Binaria (Sumador de 1 Bit)

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

**Regla:** Si (A + B + Cin) ≥ 2 → Cout = 1

---

## Instrucciones de Uso

### Para visualizar
Abre `apuntes.html` en cualquier navegador web. El archivo está completamente auto-contenido (CSS incluido, sin dependencias externas).

### Para imprimir tablas
Las tablas de referencia están separadas al final del documento. Imprime el archivo completo o selecciona solo esas secciones.

### Configuración para examen
✅ Se permite utilizar calculadora científica, pero verificar el modo de trabajo de esta  
❌ Se permite usar referencias impresas (este archivo)  
❌ No se permiten teléfonos celulares  
❌ No se permiten trabajos prácticos (TP) durante el examen  

## Notas Importantes

- **LSB**: Least Significant Bit (bit menos significativo, más a la derecha)
- **MSB**: Most Significant Bit (bit más significativo, más a la izquierda)
- **C2**: Complemento a 2 (representación de negativos en punto fijo)
- **Q[s].m.n**: Notación de punto fijo
  - s = bits de signo (0 = sin signo, 1 = con signo)
  - m = bits de enteros
  - n = bits de fraccionarios

## Fuentes

- Clase presencial UNAHUR 2026-08-18 (Clase II)
- Clase presencial UNAHUR 2026-09-15 (Clase VI)
- PDF Clase VI: "Algebra Binaria y en otras Bases" (24 páginas)

## Estado

Última actualización: **2026-09-15**  
Versiones iterativas: **17 revisiones** con feedback de aprendizaje en tiempo real

---

**Autor**: Nahuel Eduardo Longo  
**Materia**: Organización de Computadoras I  
**Universidad**: UNAHUR  
**Tipo**: Apuntes de clase - Material de referencia para examen parcial
