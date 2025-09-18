import numpy as np
import pandas as pd

# --- 1. Generar los datos base con NumPy ---
num_alumnos = 500
num_materias = 6

# Generamos la matriz de calificaciones como antes
datos_calificaciones = np.random.randint(5, 11, size=(num_alumnos, num_materias))

# --- 2. Crear un DataFrame de Pandas ---

# Para que la tabla sea legible, creamos etiquetas para las filas (índice) y las columnas
# Índice de alumnos: ['Alumno_1', 'Alumno_2', ...]
indice_alumnos = [f'Alumno_{i+1}' for i in range(num_alumnos)]

# Nombres de las columnas: ['Materia_1', 'Materia_2', ...]
nombres_materias = [f'Materia_{i+1}' for i in range(num_materias)]

# Creamos el DataFrame a partir de los datos, índices y columnas
df_calificaciones = pd.DataFrame(datos_calificaciones, index=indice_alumnos, columns=nombres_materias)


# --- 3. Manipular y buscar los datos con Pandas ---

# Las búsquedas se vuelven muy intuitivas usando los nombres que definimos
alumno_a_buscar = 'Alumno_321'
materia_a_buscar = 'Materia_5'

print("La tabla de calificaciones tiene el siguiente formato (primeras 5 filas):")
print(df_calificaciones.head())
print("\n" + "="*50 + "\n")

# Usamos el método .loc[] para buscar por etiquetas (índice y columna)
# Esta es la forma recomendada, clara y eficiente en pandas
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