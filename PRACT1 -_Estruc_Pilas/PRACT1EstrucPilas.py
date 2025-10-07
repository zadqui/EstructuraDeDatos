class Pila:
    def __init__(self, capacidad=8):
        self.capacidad = capacidad
        self.datos = []
        self.tope = 0  # posición del tope (empieza en 0)

    def insertar(self, elemento):
        if self.tope >= self.capacidad:
            print(f"DESBORDAMIENTO: No se puede insertar '{elemento}', la pila está llena.")
            return
        self.datos.append(elemento)
        self.tope += 1
        print(f"Insertar({elemento}) -> Pila: {self.datos} | TOPE={self.tope}")

    def eliminar(self, nombre_var):
        if self.tope == 0:
            print(f"SUBDESBORDAMIENTO: No se puede eliminar '{nombre_var}', la pila está vacía.")
            return
        valor = self.datos.pop()
        self.tope -= 1
        print(f"Eliminar({nombre_var}) -> {nombre_var} = {valor} | Pila: {self.datos} | TOPE={self.tope}")

    def mostrar_estado(self):
        print(f"Pila actual: {self.datos} | TOPE={self.tope}\n")


# -------------------------------------------------
# Simulación paso a paso
# -------------------------------------------------
pila = Pila()

print("Estado inicial:")
pila.mostrar_estado()

# Operaciones dadas
pila.insertar("X")   # a
pila.insertar("Y")   # b
pila.eliminar("Z")   # c
pila.eliminar("T")   # d
pila.eliminar("U")   # e
pila.insertar("V")   # f
pila.insertar("W")   # g
pila.eliminar("p")   # h
pila.insertar("R")   # i

print("\nEstado final:")
pila.mostrar_estado()

# Resultados finales
print("RESULTADOS:")
print(f"Elementos finales en la pila: {len(pila.datos)}")
print("Hubo desbordamiento o subdesbordamiento durante la ejecución.")
