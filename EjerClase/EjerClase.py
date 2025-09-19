import numpy as np
import pandas as pd


num_alumnos = 500
num_materias = 6

datos_calificaciones = np.random.randint(5, 11, size=(num_alumnos, num_materias))


indice_alumnos = [f'Alumno_{i+1}' for i in range(num_alumnos)]


nombres_materias = [f'Materia_{i+1}' for i in range(num_materias)]


df_calificaciones = pd.DataFrame(datos_calificaciones, index=indice_alumnos, columns=nombres_materias)



alumno_a_buscar = 'Alumno_321'
materia_a_buscar = 'Materia_5'

print("La tabla de calificaciones tiene el siguiente formato (primeras 5 filas):")
print(df_calificaciones.head())
print("\n" + "="*50 + "\n")

try:
    calificacion_encontrada = df_calificaciones.loc[alumno_a_buscar, materia_a_buscar]
    
    print(f"Buscando la calificación para '{alumno_a_buscar}' en la '{materia_a_buscar}'...")
    print("--------------------------------------------------")
    print(f"La calificación encontrada es: {calificacion_encontrada}")

except KeyError:
    print("El alumno o la materia no se encontró en el DataFrame.")
    
print(df_calificaciones)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(df_calificaciones)