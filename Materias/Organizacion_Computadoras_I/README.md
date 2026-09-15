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
