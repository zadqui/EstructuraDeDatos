class Pila:
    def __init__(self, nombre):
        self.nombre = nombre
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def __str__(self):
        return f"{self.nombre}: {self.items}"

def mover(origen, destino):
    disco = origen.desapilar()
    destino.apilar(disco)
    print(f"Mover disco {disco} de {origen.nombre} a {destino.nombre}")
    mostrar_torres(A, B, C)

def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        mover(origen, destino)
    else:
        hanoi(n-1, origen, destino, auxiliar)
        mover(origen, destino)
        hanoi(n-1, auxiliar, origen, destino)

def mostrar_torres(A, B, C):
    print(f"{A}\n{B}\n{C}\n")


A = Pila("A")
B = Pila("B")
C = Pila("C")


for disco in range(3, 0, -1):
    A.apilar(disco)

print("Estado inicial:")
mostrar_torres(A, B, C)

hanoi(3, A, B, C)
