import numpy as np

# Definimos meses y departamentos
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
departamentos = ["Ropa", "Deportes", "Juguetería"]

# Creamos una matriz de 12x3 inicializada en 0
ventas = np.zeros((12, 3), dtype=int)

# 1. Insertar venta
def insertar_venta(mes, departamento, valor):
    i = meses.index(mes)
    j = departamentos.index(departamento)
    ventas[i, j] = valor

# 2. Buscar venta
def buscar_venta(mes, departamento):
    i = meses.index(mes)
    j = departamentos.index(departamento)
    return ventas[i, j]

# 3. Eliminar venta
def eliminar_venta(mes, departamento):
    i = meses.index(mes)
    j = departamentos.index(departamento)
    ventas[i, j] = 0

# 4. Mostrar tabla
def mostrar_tabla():
    print(f"{'Mes':<12} {'Ropa':<10} {'Deportes':<10} {'Juguetería':<12}")
    print("-" * 44)
    for i, mes in enumerate(meses):
        print(f"{mes:<12} {ventas[i,0]:<10} {ventas[i,1]:<10} {ventas[i,2]:<12}")

# --- Ejemplo ---
insertar_venta("Enero", "Ropa", 1500)
insertar_venta("Febrero", "Deportes", 2200)
insertar_venta("Marzo", "Juguetería", 1800)

mostrar_tabla()

print("\nBuscar Febrero-Deportes:", buscar_venta("Febrero", "Deportes"))
eliminar_venta("Enero", "Ropa")
print("Después de eliminar Enero-Ropa:", buscar_venta("Enero", "Ropa"))
