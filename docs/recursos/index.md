# Recursos de Referencia

Tablas, equivalencias y herramientas para consulta rápida durante el estudio.

## Disponible en Esta Sección

### 1. [Tabla de Equivalencias (0-255)](tabla-equivalencias.md)
Tabla completa de conversiones entre Decimal, Binario, Octal y Hexadecimal para todos los números del 0 al 255.

**Úsalo para:**
- Verificar conversiones que hayas hecho
- Encontrar equivalencias rápidamente
- Reconocer patrones en conversiones
- Estudiar la relación entre sistemas

**Contenido:**
- Segmentos por rangos (0-15, 16-31, etc.)
- Tabla de potencias de 2 en cada sistema
- Patrones útiles de reconocimiento rápido
- Números especiales ($2^n - 1$)

### 2. [Unidades de Almacenamiento Binario](unidades-almacenamiento.md)
Jerarquía completa de unidades desde bits hasta Yottabytes, todas basadas en potencias de 2.

**Úsalo para:**
- Comprender las unidades informáticas (KiB, MiB, GiB, etc.)
- Convertir entre unidades de almacenamiento
- Entender el contexto práctico de potencias de 2
- Resolver problemas de almacenamiento

**Contenido:**
- Tabla de equivalencias en bytes
- Potencias de 2 (desde $2^{10}$ a $2^{80}$)
- Diferencia entre binario (KiB) y decimal (KB)
- Conversiones comunes y aplicaciones prácticas

## Cómo Usar Estos Recursos

### Durante la Clase
- Usa la [Tabla de Equivalencias](tabla-equivalencias.md) para verificar rápidamente tus conversiones
- Consulta las potencias en ambas tablas para evitar cálculos repetitivos
- Identifica patrones usando los ejemplos de reconocimiento rápido

### Estudiando para el Parcial
1. Intenta resolver un ejercicio **sin** consultar recursos
2. Verifica tu respuesta usando la [Tabla de Equivalencias](tabla-equivalencias.md)
3. Si cometiste un error, entiende **dónde** y **por qué** fallaste
4. Practica el mismo tipo de ejercicio nuevamente

### Cuando Necesites Ayuda
- ¿No recuerdas qué es $(101110)_2$ en decimal? Busca en la tabla
- ¿Necesitas convertir 2 GiB a bytes? Usa la tabla de [Unidades de Almacenamiento](unidades-almacenamiento.md)
- ¿Quieres ver todos los valores hexadecimales de un byte? Mira la tabla de dígitos hexadecimales

## Tablas Rápidas de Referencia

### Potencias de 2 Esenciales

```
2^0  = 1
2^1  = 2
2^2  = 4
2^3  = 8
2^4  = 16
2^5  = 32
2^6  = 64
2^7  = 128
2^8  = 256 (1 Byte)
2^10 = 1,024 (1 KiB)
2^20 = 1,048,576 (1 MiB)
2^30 = 1,073,741,824 (1 GiB)
```

### Agrupación Rápida para Conversiones

**Binario ↔ Octal:** Grupos de 3 bits
```
(110)(101)₂ = (6)(5)₈
```

**Binario ↔ Hexadecimal:** Grupos de 4 bits
```
(1101)(0101)₂ = (D)(5)₁₆
```

### Números Especiales

**Todos 1s = $2^n - 1$:**
```
(1)₂ = 1 = 2¹ - 1
(11)₂ = 3 = 2² - 1
(111)₂ = 7 = 2³ - 1
(1111)₂ = 15 = 2⁴ - 1
(11111111)₂ = 255 = 2⁸ - 1
```

**Potencias de 2 = 1 seguido de ceros:**
```
(1)₂ = 1 = 2⁰
(10)₂ = 2 = 2¹
(100)₂ = 4 = 2²
(1000)₂ = 8 = 2³
(10000000)₂ = 128 = 2⁷
```

## Contexto: Por Qué Estos Recursos Importan

### Tabla de Equivalencias (0-255)
- Un byte puede representar 256 valores diferentes
- Este rango es fundamental en informática (píxeles, caracteres ASCII, etc.)
- Memorizar algunos de estos valores te ayuda a estimar conversiones rápidamente

### Unidades de Almacenamiento
- Los sistemas reales usan estas unidades constantemente
- Entender potencias de 2 aquí te prepara para informática avanzada
- La diferencia entre KiB y KB tiene implicaciones prácticas reales

## Recomendación de Estudio

1. **Primera vez:** Lee ambas tablas para familiarizarte con la estructura
2. **Mientras practicas:** Usa las tablas para verificar, no para evitar pensar
3. **Para memorizar:** Aprende las potencias de 2 hasta $2^{10}$ de memoria
4. **Antes del parcial:** Verifica que entiendas **por qué** cada equivalencia es correcta (aplicando Teorema Fundamental)

---

**Volver a:** [Ejercicios](../ejercicios/index.md) | [Clase II](../clase-ii/index.md)
