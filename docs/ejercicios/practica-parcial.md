# Ejercicios de Práctica para Parcial

Estos ejercicios son similares a los que pueden aparecer en el examen parcial. Resuélvelos aplicando el Teorema Fundamental y los métodos de conversión aprendidos.

---

## Ejercicio 1: Conversión Múltiple con Fracciones

**Enunciado:** Convertir $(1101.11)_2$ a decimal y luego verificar el resultado convertiendo a hexadecimal.

**Solución paso a paso:**

**Parte 1: Binario → Decimal (usando Teorema Fundamental)**

$$(1101.11)_2 = 1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 + 1 \cdot 2^{-1} + 1 \cdot 2^{-2}$$

$$= 1 \cdot 8 + 1 \cdot 4 + 0 \cdot 2 + 1 \cdot 1 + 1 \cdot 0.5 + 1 \cdot 0.25$$

$$= 8 + 4 + 1 + 0.5 + 0.25 = 13.75$$

**Parte 2: Verificación por agrupación (Binario → Hexadecimal)**

Agrupar en 4 dígitos binarios: $(1101.11)_2 = (1101).(1100)_2 = (D).(C)_{16}$

Verificando:
- $(D)_{16} = 13_{10}$ (parte entera)
- $(0.C)_{16} = 0 \cdot 16^0 + 12 \cdot 16^{-1} = 0.75_{10}$ (parte fraccionaria)
- Total: $13 + 0.75 = 13.75_{10}$ ✓

**Respuesta:** $(1101.11)_2 = (13.75)_{10} = (D.C)_{16}$ ✓

---

## Ejercicio 2: Encontrar Base Desconocida

**Enunciado:** Si $(102)_B = (11)_{10}$, ¿cuál es la base $B$?

**Solución:**

Aplicar el Teorema Fundamental:

$$(102)_B = 1 \cdot B^2 + 0 \cdot B^1 + 2 \cdot B^0 = 11$$

$$B^2 + 2 = 11$$

$$B^2 = 9$$

$$B = 3$$ (tomamos la raíz positiva)

**Verificación:** $(102)_3 = 1 \cdot 3^2 + 0 \cdot 3^1 + 2 \cdot 3^0 = 9 + 0 + 2 = 11$ ✓

**Condición:** B debe ser mayor que 2 (el dígito mayor en $(102)_B$) ✓

**Respuesta:** $B = 3$ (Sistema Ternario) ✓

---

## Ejercicio 3: Conversión Octal → Hexadecimal

**Enunciado:** Convertir $(573)_8$ a hexadecimal sin pasar por decimal (usando pasaje rápido).

**Solución:**

**Paso 1: Octal → Binario** (expandir cada dígito octal a 3 bits binarios)

- $(5)_8 = (101)_2$
- $(7)_8 = (111)_2$
- $(3)_8 = (011)_2$

Resultado: $(573)_8 = (101111011)_2$

**Paso 2: Binario → Hexadecimal** (agrupar en 4 bits de derecha a izquierda)

$(101111011)_2 = (0001)(0111)(1011)_2$

Agregar cero a la izquierda si es necesario.

**Paso 3: Convertir grupos a hexadecimal**

- $(0001)_2 = 1_{16}$
- $(0111)_2 = 7_{16}$
- $(1011)_2 = B_{16}$

Resultado: $(573)_8 = (17B)_{16}$

**Verificación por Decimal:**

$(573)_8 = 5 \cdot 8^2 + 7 \cdot 8^1 + 3 \cdot 8^0 = 5 \cdot 64 + 7 \cdot 8 + 3 = 320 + 56 + 3 = 379_{10}$

$(17B)_{16} = 1 \cdot 16^2 + 7 \cdot 16^1 + 11 \cdot 16^0 = 256 + 112 + 11 = 379_{10}$ ✓

**Respuesta:** $(573)_8 = (17B)_{16}$ ✓

---

## Ejercicio 4: División Sucesiva (Decimal → Binario)

**Enunciado:** Convertir $(45)_{10}$ a binario usando división sucesiva. Verificar aplicando Teorema Fundamental.

**Solución:**

**Paso 1: División Sucesiva**

```
45 ÷ 2 = 22 resto 1
22 ÷ 2 = 11 resto 0
11 ÷ 2 = 5  resto 1
5  ÷ 2 = 2  resto 1
2  ÷ 2 = 1  resto 0
1  ÷ 2 = 0  resto 1
```

Leyendo restos de abajo hacia arriba: $(45)_{10} = (101101)_2$

**Paso 2: Verificación por Teorema Fundamental**

$$(101101)_2 = 1 \cdot 2^5 + 0 \cdot 2^4 + 1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0$$

$$= 1 \cdot 32 + 0 + 1 \cdot 8 + 1 \cdot 4 + 0 + 1 \cdot 1$$

$$= 32 + 8 + 4 + 1 = 45_{10}$$ ✓

**Respuesta:** $(45)_{10} = (101101)_2$ ✓

---

## Ejercicio 5: Conversión Fraccionaria Binaria

**Enunciado:** Convertir $(0.6875)_{10}$ a binario usando multiplicación sucesiva.

**Solución:**

**Pasos:**

```
0.6875 × 2 = 1.375    → dígito: 1 (parte entera)
0.375  × 2 = 0.75     → dígito: 0
0.75   × 2 = 1.5      → dígito: 1
0.5    × 2 = 1.0      → dígito: 1 (fracción = 0, terminamos)
```

Leyendo de arriba hacia abajo: $(0.6875)_{10} = (0.1011)_2$

**Verificación por Teorema Fundamental:**

$$(0.1011)_2 = 1 \cdot 2^{-1} + 0 \cdot 2^{-2} + 1 \cdot 2^{-3} + 1 \cdot 2^{-4}$$

$$= 1 \cdot 0.5 + 0 + 1 \cdot 0.125 + 1 \cdot 0.0625$$

$$= 0.5 + 0.125 + 0.0625 = 0.6875_{10}$$ ✓

**Respuesta:** $(0.6875)_{10} = (0.1011)_2$ ✓

---

## Consejos para el Parcial

1. **Siempre verifica:** Usa el Teorema Fundamental para comprobar conversiones
2. **Elige el método apropiado:** 
   - Cualquier base → Decimal: Teorema Fundamental
   - Decimal → Cualquier base: División sucesiva
   - Binario ↔ Octal/Hex: Agrupación directa
3. **Mantén orden:** Escribe paso a paso para evitar errores
4. **Identifica bases:** Asegúrate de indicar claramente la base de cada número $(N)_B$
5. **Fracciones:** Recuerda que exponentes negativos ($2^{-1}, 2^{-2}$, etc.) representan fracciones
