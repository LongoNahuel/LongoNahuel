# Fundamentos - Estructuras Numéricas y Sistemas de Numeración

## Estructuras Numéricas

### Números Naturales (ℕ)
```
ℕ = {0, 1, 2, 3, 4, ...}
```
- Usados para contar
- No incluyen negativos
- Base para otras estructuras

### Números Enteros (ℤ)
```
ℤ = {..., -3, -2, -1, 0, 1, 2, 3, ...}
```
- Incluyen positivos, negativos y cero
- Permiten restar sin restricción

### Números Racionales (ℚ)
```
ℚ = {p/q : p ∈ ℤ, q ∈ ℕ, q ≠ 0}
```
- Fracciones y decimales finitos
- Decimales periódicos exactos

### Números Reales (ℝ)
```
ℝ = ℚ ∪ {números irracionales}
```
- Incluyen decimales periódicos infinitos
- Números irracionales (π, e, √2)

---

## Sistemas Numéricos

### Sistema Binario (Base 2)

**Símbolos**: 0, 1

**Ejemplo**: (1011)₂

**Conversión a decimal**:
```
(1011)₂ = 1·2³ + 0·2² + 1·2¹ + 1·2⁰
        = 1·8 + 0·4 + 1·2 + 1·1
        = 8 + 2 + 1
        = 11₁₀
```

### Sistema Decimal (Base 10)

**Símbolos**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

**Ejemplo**: (234)₁₀

**Estructura posicional**:
```
234₁₀ = 2·10² + 3·10¹ + 4·10⁰
      = 200 + 30 + 4
```

### Sistema Hexadecimal (Base 16)

**Símbolos**: 0-9, A(10), B(11), C(12), D(13), E(14), F(15)

**Ejemplo**: (1A3F)₁₆

**Conversión a decimal**:
```
(1A3F)₁₆ = 1·16³ + 10·16² + 3·16¹ + 15·16⁰
         = 4096 + 2560 + 48 + 15
         = 6719₁₀
```

### Sistema Octal (Base 8)

**Símbolos**: 0, 1, 2, 3, 4, 5, 6, 7

**Ejemplo**: (1734)₈

**Conversión a decimal**:
```
(1734)₈ = 1·8³ + 7·8² + 3·8¹ + 4·8⁰
        = 512 + 448 + 24 + 4
        = 988₁₀
```

---

## Teorema Fundamental de la Enumeración

### Fórmula General

Para convertir un número en base **b** a base 10:

$$A_b = \sum_{i=-m}^{n-1} a_i \cdot b^i$$

Donde:
- **b** = base del sistema
- **a_i** = dígito en posición i
- **n** = cantidad de dígitos enteros
- **m** = cantidad de dígitos fraccionarios

### Aplicación Práctica

**Ejemplo en base 5**:
```
(302,14)₅ = 3·5² + 0·5¹ + 2·5⁰ + 1·5⁻¹ + 4·5⁻²
          = 3·25 + 0 + 2 + 1/5 + 4/25
          = 75 + 2 + 0,2 + 0,16
          = 77,36₁₀
```

---

## Conversiones de Bases

### Decimal a Binario (Método de División)

**Parte entera: Divisiones sucesivas por 2**

```
85 ÷ 2 = 42 resto 1
42 ÷ 2 = 21 resto 0
21 ÷ 2 = 10 resto 1
10 ÷ 2 = 5 resto 0
5 ÷ 2 = 2 resto 1
2 ÷ 2 = 1 resto 0
1 ÷ 2 = 0 resto 1

Resultado (leer de abajo a arriba): (1010101)₂
```

**Parte fraccionaria: Multiplicaciones sucesivas por 2**

```
0,625 × 2 = 1,25  → bit = 1
0,25 × 2 = 0,5    → bit = 0
0,5 × 2 = 1,0     → bit = 1

Resultado: (101)₂
```

### Binario a Decimal (Suma de Potencias)

```
(11010,101)₂ = 1·2⁴ + 1·2³ + 0·2² + 1·2¹ + 0·2⁰ + 1·2⁻¹ + 0·2⁻² + 1·2⁻³
             = 16 + 8 + 2 + 0,5 + 0,125
             = 26,625₁₀
```

### Binario ↔ Hexadecimal (Conversión Directa)

**Agrupar de 4 en 4 bits desde la derecha**:

```
(10110111)₂ = (1011|0111)₂ = (B7)₁₆

1011₂ = 1·8 + 0·4 + 1·2 + 1·1 = 11 = B₁₆
0111₂ = 0·8 + 1·4 + 1·2 + 1·1 = 7₁₆
```

---

## Unidades de Almacenamiento Binario

| Nombre | Equivalencia | Bits |
|--------|-------------|------|
| **Bit** | Unidad básica | 1 |
| **Nibble** | Medio byte | 4 |
| **Byte** | 8 bits | 8 |
| **Word** | 2 bytes | 16 |
| **DWORD** | 4 bytes | 32 |
| **QWORD** | 8 bytes | 64 |

---

## Propiedades de la Potenciación

### Potencias de 2 (Memorizar)

```
2⁰ = 1
2¹ = 2
2² = 4
2³ = 8
2⁴ = 16
2⁵ = 32
2⁶ = 64
2⁷ = 128
2⁸ = 256
2⁹ = 512
2¹⁰ = 1024
```

### Reglas Básicas

```
2ᵃ · 2ᵇ = 2⁽ᵃ⁺ᵇ⁾
2ᵃ ÷ 2ᵇ = 2⁽ᵃ⁻ᵇ⁾
(2ᵃ)ᵇ = 2⁽ᵃ·ᵇ⁾
2⁻ᵃ = 1/(2ᵃ)
```

---

## Próxima Sección

→ [[02-Algebra-Binaria|Álgebra Binaria y Operaciones]]
