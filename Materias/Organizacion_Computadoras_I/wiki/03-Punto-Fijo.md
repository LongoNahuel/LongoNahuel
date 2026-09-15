# Notación Q - Punto Fijo

## Formato Q[s].m.n

**Estructura**: `Q[s].m.n`

- **s** = cantidad de bits para signo (0 o 1)
  - s=0: sin signo (solo positivos)
  - s=1: con signo (positivos y negativos en CA2)
- **m** = cantidad de bits para parte entera
- **n** = cantidad de bits para parte fraccionaria

### Ejemplos

| Formato | Descripción | Rango |
|---------|-------------|-------|
| Q0.10.4 | Sin signo, 10 enteros, 4 fraccionarios | 0 a 1023,9375 |
| Q1.7.4  | Con signo, 7 enteros, 4 fraccionarios | -128 a +127,9375 |
| Q1.8.5  | Con signo, 8 enteros, 5 fraccionarios | -256 a +255,96875 |

## Factor de Escala

**Regla**: Factor de escala = **2^n** (depende SOLO de bits fraccionarios)

### Aplicación

Para operar en punto fijo:
1. Multiplicar por factor de escala → obtener entero
2. Realizar operaciones (suma, resta)
3. Dividir por factor de escala → volver a punto fijo

**Ejemplo en Q0.10.4**:
```
Factor = 2⁴ = 16

A = 279,75₁₀
A × 16 = 4476₁₀

B = 179,7₁₀
B × 16 = 2875,2 ≈ 2875₁₀

Suma: 4476 + 2875 = 7351₁₀
Dividir: 7351 ÷ 16 = 459,4375₁₀
```

## Complemento a 2 (CA2)

### Para Números Positivos

Representar directamente en binario con BMS=0

**Ejemplo**: +5 en 4 bits
```
+5 = (0101)₂
```

### Para Números Negativos

Aplicar CA2: **NOT(número positivo) + 1**

**Ejemplo**: -5 en 4 bits
```
Paso 1: Representar +5 = (0101)₂
Paso 2: NOT(0101) = (1010)₂
Paso 3: (1010) + 1 = (1011)₂
-5 = (1011)₂
```

### Descomplementación (Volver a Decimal)

Si el resultado tiene BMS=1 (es negativo):
```
Valor = NOT(resultado) + 1
```

**Ejemplo**: (1011)₂ a decimal
```
NOT(1011) = (0100)₂
(0100) + 1 = (0101)₂ = 5₁₀
Entonces (1011)₂ = -5₁₀
```

## Próxima Sección

→ [[04-Overflow|Detección de Overflow]]
