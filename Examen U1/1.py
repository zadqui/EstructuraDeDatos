def pedir_datos():
    n = int(input("¿Cuántos nombres deseas ingresar?: "))
    
    nombres = []
    longitudes = []
    
    for i in range(n):
        nombre = input(f"Ingresa el nombre {i+1}: ")
        nombres.append(nombre)
        longitudes.append(len(nombre))  
    
    return nombres, longitudes

def mostrar_datos(nombres, longitudes):
    print("\n--- Resultados ---")
    for i in range(len(nombres)):
        print(f"Nombre: {nombres[i]} | Longitud: {longitudes[i]}")


nombres, longitudes = pedir_datos()
mostrar_datos(nombres, longitudes)
