# Clase II: Sistemas de Numeración

Contenido completo de la Clase II - Organización de Computadoras I.

## Temas Principales

Esta sección cubre los fundamentos teóricos de los sistemas numéricos posicionales, con énfasis en el **Teorema Fundamental de la Enumeración** como método universal de conversión.

### 1. [Estructura Numérica](estructura-numerica.md)
Propiedades fundamentales de los números: conmutativa, asociativa, distributiva. Jerarquía de conjuntos numéricos (ℕ, ℤ, ℚ, ℝ).

### 2. [Potenciación](potenciacion.md)
Propiedades de las potencias: potencia cero, potencia de potencia, exponentes negativos. Aplicación en sistemas numéricos.

### 3. [Sistemas Numéricos](sistemas-numericos.md)
Introducción a los Sistemas de Notación Posicional (SNP). Sistemas principales: Decimal, Binario, Octal, Hexadecimal, Base-64.

### 4. [Teorema Fundamental](teorema-fundamental.md)
**El concepto clave:** Una única fórmula para convertir cualquier base a decimal. $$N = \sum_{i=-m}^{n-1} A_i \cdot B^i$$

### 5. [Métodos de Conversión](conversiones.md)
Estrategias prácticas:
- Cualquier base → Decimal (Teorema Fundamental)
- Decimal → Cualquier base (División/Multiplicación sucesiva)
- Pasajes rápidos (Binario ↔ Octal/Hexadecimal)

### 6. [Tablas Rápidas](tablas-rapidas.md)
Referencia de potencias de 2, 8, 16, 10. Tablas de equivalencias y dígitos hexadecimales/octales.

## Concepto Clave

El **Teorema Fundamental de la Enumeración** es el hilo conductor de toda la clase. No hay múltiples métodos diferentes: hay UN método (el Teorema) que funciona para cualquier base, y luego métodos específicos para optimizar conversiones comunes.

## Flujo de Aprendizaje Recomendado

1. Comienza con **Estructura Numérica** para entender las bases matemáticas
2. Repasa **Potenciación** (especialmente exponentes negativos)
3. Lee **Sistemas Numéricos** para ver qué es cada base
4. Domina el **Teorema Fundamental** — este es tu herramienta principal
5. Aprende los **Métodos de Conversión** específicos para ganar velocidad
6. Usa las **Tablas Rápidas** como referencia durante ejercicios

## Resumen de Fórmulas Esenciales

### Teorema Fundamental
$$N = \sum_{i=-m}^{n-1} A_i \cdot B^i = A_{n-1} B^{n-1} + \ldots + A_0 B^0 + A_{-1} B^{-1} + \ldots + A_{-m} B^{-m}$$

### Conversión Decimal → Base B (Parte Entera)
1. Dividir entre B
2. Anotar resto
3. Repetir hasta cociente = 0
4. Leer restos de abajo hacia arriba

### Conversión Decimal → Base B (Parte Fraccionaria)
1. Multiplicar por B
2. Anotar parte entera
3. Usar parte fraccionaria
4. Repetir hasta precisión deseada
5. Leer dígitos de arriba hacia abajo

## Equivalencias de Bases Rápidas

| Binario | Octal | Decimal | Hexadecimal |
|---------|-------|---------|-------------|
| 0000 | 0 | 0 | 0 |
| 0001 | 1 | 1 | 1 |
| 0010 | 2 | 2 | 2 |
| 0011 | 3 | 3 | 3 |
| 0100 | 4 | 4 | 4 |
| 0101 | 5 | 5 | 5 |
| 0110 | 6 | 6 | 6 |
| 0111 | 7 | 7 | 7 |
| 1000 | 10 | 8 | 8 |
| 1001 | 11 | 9 | 9 |
| 1010 | 12 | 10 | A |
| 1011 | 13 | 11 | B |
| 1100 | 14 | 12 | C |
| 1101 | 15 | 13 | D |
| 1110 | 16 | 14 | E |
| 1111 | 17 | 15 | F |

Continúa a los [Ejercicios](../ejercicios/index.md) para practicar estos conceptos.
