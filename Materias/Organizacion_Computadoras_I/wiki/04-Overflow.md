# Detección de Overflow

## Concepto Fundamental

**Overflow** (Desborde): Ocurre cuando el resultado de una operación **excede el rango válido** del formato.

### Causa Principal

Operandos del **mismo signo** producen resultado de **signo opuesto**.

## Método 1: Comparación de Signos (Rápido)

### Regla

```
OVERFLOW = (BMS_A = BMS_B) AND (BMS_Y ≠ BMS_A)
```

Traducido: Dos operandos del mismo signo dan resultado de signo distinto.

### Casos

| A | B | Resultado | ¿Overflow? |
|---|---|-----------|-----------|
| + | + | + | NO |
| + | + | - | ✅ SÍ |
| - | - | - | NO |
| - | - | + | ✅ SÍ |
| + | - | + o - | NO |
| - | + | + o - | NO |

### Ejemplo

```
5 + 4 = 9 (en 4 bits, rango -8 a +7)
A = (0101)₂ (positivo)
B = (0100)₂ (positivo)
Y = (1001)₂ (negativo)

Conclusión: Dos positivos dan resultado negativo → OVERFLOW
```

## Método 2: Análisis de Acarreos (Riguroso)

### Regla

```
OVERFLOW = (BMS_A = BMS_B) AND (Cin_BMS ≠ Cout_BMS)
```

Donde:
- **Cin_BMS** = acarreo que ENTRA al bit de signo
- **Cout_BMS** = acarreo que SALE del bit de signo

### Paso a Paso

1. Identificar la columna del BMS
2. Anotar Cin_BMS (acarreo de la columna anterior)
3. Anotar Cout_BMS (acarreo generado en esa columna)
4. Si son distintos Y los operandos tienen igual signo → OVERFLOW

### Ejemplo

```
119 + 40 = 159 (en 8 bits, rango -128 a +127)

    ¹0110000  ← Acarreos
    0111 0111  (119)
  + 0010 1000  (40)
  ───────────
    1001 1111  (resultado)

Análisis del BMS (columna 8):
Cin_BMS = 1 (acarreo entrante)
Cout_BMS = 0 (acarreo saliente)
1 ≠ 0 → OVERFLOW DETECTADO
```

## Próxima Sección

→ [[05-Ejercicios-Resueltos|Ejercicios de Examen - Soluciones Detalladas]]
