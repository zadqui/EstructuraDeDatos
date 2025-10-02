# Evaluador de Expresiones con Pila

Este programa en Python permite **convertir y evaluar expresiones aritméticas** en distintas notaciones usando una **estructura de pila**.

## Funcionalidad

1. El usuario ingresa una **expresión en notación infija** (ejemplo: `( 3 + 4 ) * 2`).
2. El programa convierte la expresión a:
   - **Posfija** (notación polaca inversa).
   - **Prefija** (notación polaca normal).
3. Se evalúan las dos notaciones con ayuda de una **pila**.
4. Se muestra el resultado en pantalla.

---

## Ejemplo de uso

```
Ingresa expresión infija (usa espacios, ej: ( 3 + 4 ) * 2 ): ( 3 + 4 ) * 2

Posfija: 3 4 + 2 *
Prefija: * + 3 4 2
Evaluación Posfija: 14
Evaluación Prefija: 14
```

---

## Requisitos

- Python 3.x

---

## Ejecución

1. Clona este repositorio o descarga el archivo `.py`.
2. En consola, navega hasta la carpeta del proyecto.
3. Ejecuta:

```bash
python evaluador.py
```

---

## Notaciones

- **Infija**: la que usamos normalmente, con operadores entre operandos.  
  Ejemplo: `( 3 + 4 ) * 2`

- **Posfija (RPN)**: el operador va después de los operandos.  
  Ejemplo: `3 4 + 2 *`

- **Prefija (PN)**: el operador va antes de los operandos.  
  Ejemplo: `* + 3 4 2`

---

## Autor

Proyecto académico desarrollado para la materia de **Estructura de Datos**, con el fin de practicar el uso de **pilas** en la evaluación de expresiones aritméticas.
