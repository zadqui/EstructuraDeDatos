pila = []

def hacer_accion(accion):
    pila.append(accion)
    print(f"Acción realizada: {accion}")

def deshacer():
    if len(pila) == 0:
        print("No hay acciones para deshacer")
    else:
        accion = pila.pop()
        print(f"Deshacer: {accion}")


hacer_accion("Escribió 'Hola'")
hacer_accion("Agregó ' mundo'")
hacer_accion("Borró 'o'")

print("\n--- Estado de la pila ---")
print(pila)

print("\n--- Deshacer acciones ---")
deshacer()
deshacer()
deshacer()
deshacer()  