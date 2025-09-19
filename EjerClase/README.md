# Sistema de Calificaciones con NumPy y Pandas

Este proyecto implementa un sistema de generación y gestión de calificaciones utilizando Python.  
El código simula las notas de 500 alumnos en 6 materias, organiza los datos en una tabla con Pandas y permite buscar calificaciones específicas.


## Descripción del código
1. **Generación de datos aleatorios**  
   - Se crean 500 alumnos × 6 materias con valores entre 5 y 10.  
   - Cada fila representa un alumno y cada columna una materia.

2. **Construcción del DataFrame**  
   - Los datos se organizan en una tabla usando `pandas.DataFrame`.  
   - Filas → `Alumno_1` ... `Alumno_500`  
   - Columnas → `Materia_1` ... `Materia_6`

3. **Búsqueda de calificaciones**  
   - Se selecciona un alumno y una materia concretos (`Alumno_321`, `Materia_5`).  
   - El programa obtiene la calificación correspondiente mediante `.loc`.

4. **Visualización**  
   - Vista previa con las primeras 5 filas (`.head()`).  
   - Posibilidad de mostrar toda la tabla ajustando las opciones de Pandas.  

---
## Ejemplo de salida
La tabla de calificaciones tiene el siguiente formato (primeras 5 filas):
Materia_1 Materia_2 Materia_3 Materia_4 Materia_5 Materia_6
Alumno_1 8 7 9 6 5 10
Alumno_2 6 10 7 8 9 5
Alumno_3 9 8 6 7 8 10
Alumno_4 10 9 5 8 7 6
Alumno_5 7 8 9 6 6 8
Buscando la calificación para 'Alumno_321' en la 'Materia_5'...

La calificación encontrada es: 8
