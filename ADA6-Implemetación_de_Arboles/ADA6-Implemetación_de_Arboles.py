
from collections import deque

# ------------------------------------------------------------
# Clase Nodo
# ------------------------------------------------------------
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None


# ------------------------------------------------------------
# Clase Árbol Binario de Búsqueda
# ------------------------------------------------------------
class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    # [0] Verifica si el árbol está vacío
    def esVacio(self):
        return self.raiz is None

    # [1] Insertar elemento
    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(self.raiz, dato)

    def _insertar(self, actual, dato):
        if dato < actual.dato:
            if actual.izq is None:
                actual.izq = Nodo(dato)
            else:
                self._insertar(actual.izq, dato)
        elif dato > actual.dato:
            if actual.der is None:
                actual.der = Nodo(dato)
            else:
                self._insertar(actual.der, dato)

    # [2] Mostrar árbol acostado
    def mostrar(self, nodo=None, nivel=0):
        # Evita reiniciar desde la raíz en llamadas recursivas
        if nodo is None and nivel == 0:
            nodo = self.raiz
        if nodo is None:
            return
        self.mostrar(nodo.der, nivel + 1)
        print("   " * nivel + f"{nodo.dato}")
        self.mostrar(nodo.izq, nivel + 1)

    # [3] Graficar árbol vertical (texto)
    def graficar(self, nodo=None, nivel=0, prefijo="Raíz: "):
        if nodo is None and nivel == 0:
            nodo = self.raiz
        if nodo is None:
            return
        print(" " * (4 * nivel) + prefijo + str(nodo.dato))
        if nodo.izq:
            self.graficar(nodo.izq, nivel + 1, "Izq -> ")
        if nodo.der:
            self.graficar(nodo.der, nivel + 1, "Der -> ")

    # [4] Buscar elemento
    def buscar(self, dato):
        return self._buscar(self.raiz, dato)

    def _buscar(self, actual, dato):
        if actual is None:
            return False
        if actual.dato == dato:
            return True
        elif dato < actual.dato:
            return self._buscar(actual.izq, dato)
        else:
            return self._buscar(actual.der, dato)

    # [5] Recorrido PreOrden
    def preOrden(self, nodo):
        if nodo:
            print(nodo.dato, end=" ")
            self.preOrden(nodo.izq)
            self.preOrden(nodo.der)

    # [6] Recorrido InOrden
    def inOrden(self, nodo):
        if nodo:
            self.inOrden(nodo.izq)
            print(nodo.dato, end=" ")
            self.inOrden(nodo.der)

    # [7] Recorrido PostOrden
    def postOrden(self, nodo):
        if nodo:
            self.postOrden(nodo.izq)
            self.postOrden(nodo.der)
            print(nodo.dato, end=" ")

    # [8] Eliminar nodo por PREDECESOR
    def eliminarPredecesor(self, dato):
        self.raiz = self._eliminar(self.raiz, dato, usar_predecesor=True)

    # [9] Eliminar nodo por SUCESOR
    def eliminarSucesor(self, dato):
        self.raiz = self._eliminar(self.raiz, dato, usar_predecesor=False)

    def _eliminar(self, nodo, dato, usar_predecesor):
        if nodo is None:
            return nodo
        if dato < nodo.dato:
            nodo.izq = self._eliminar(nodo.izq, dato, usar_predecesor)
        elif dato > nodo.dato:
            nodo.der = self._eliminar(nodo.der, dato, usar_predecesor)
        else:
            # Nodo encontrado
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            if usar_predecesor:
                predecesor = self._maximo(nodo.izq)
                nodo.dato = predecesor.dato
                nodo.izq = self._eliminar(nodo.izq, predecesor.dato, usar_predecesor)
            else:
                sucesor = self._minimo(nodo.der)
                nodo.dato = sucesor.dato
                nodo.der = self._eliminar(nodo.der, sucesor.dato, usar_predecesor)
        return nodo

    def _minimo(self, nodo):
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    def _maximo(self, nodo):
        while nodo.der:
            nodo = nodo.der
        return nodo

    # [10] Recorrido por niveles
    def recorridoNiveles(self):
        if self.raiz is None:
            print("El árbol está vacío.")
            return
        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            print(actual.dato, end=" ")
            if actual.izq:
                cola.append(actual.izq)
            if actual.der:
                cola.append(actual.der)
        print()

    # [11] Altura del árbol
    def altura(self, nodo=None, nivel=0):
        if nodo is None and nivel == 0:
            nodo = self.raiz
        if nodo is None:
            return 0
        alt_izq = self.altura(nodo.izq, nivel + 1)
        alt_der = self.altura(nodo.der, nivel + 1)
        return 1 + max(alt_izq, alt_der)

    # [12] Cantidad de hojas
    def contarHojas(self, nodo=None, nivel=0):
        if nodo is None and nivel == 0:
            nodo = self.raiz
        if nodo is None:
            return 0
        if nodo.izq is None and nodo.der is None:
            return 1
        return self.contarHojas(nodo.izq, nivel + 1) + self.contarHojas(nodo.der, nivel + 1)

    # [13] Cantidad de nodos
    def contarNodos(self, nodo=None, nivel=0):
        if nodo is None and nivel == 0:
            nodo = self.raiz
        if nodo is None:
            return 0
        return 1 + self.contarNodos(nodo.izq, nivel + 1) + self.contarNodos(nodo.der, nivel + 1)

    # [15] Árbol binario completo
    def esCompleto(self):
        if self.raiz is None:
            return True
        cola = deque([self.raiz])
        encontradoHueco = False
        while cola:
            actual = cola.popleft()
            if actual.izq:
                if encontradoHueco:
                    return False
                cola.append(actual.izq)
            else:
                encontradoHueco = True
            if actual.der:
                if encontradoHueco:
                    return False
                cola.append(actual.der)
            else:
                encontradoHueco = True
        return True

    # [16] Árbol binario lleno (corregido con control de nivel)
    def esLleno(self, nodo=None, nivel=0):
        if nodo is None and nivel == 0:
            nodo = self.raiz
        if nodo is None:
            return True
        if (nodo.izq is None) != (nodo.der is None):
            return False
        return self.esLleno(nodo.izq, nivel + 1) and self.esLleno(nodo.der, nivel + 1)

    # [17] Eliminar todo el árbol
    def eliminarArbol(self):
        self.raiz = None
        print("🌲 Árbol eliminado completamente.")


# ------------------------------------------------------------
# Menú principal
# ------------------------------------------------------------
if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()

    while True:
        print("\n===== MENÚ ÁRBOL BINARIO =====")
        print("1. Insertar elemento")
        print("2. Mostrar árbol acostado")
        print("3. Graficar árbol vertical")
        print("4. Buscar elemento")
        print("5. Recorrido PreOrden")
        print("6. Recorrido InOrden")
        print("7. Recorrido PostOrden")
        print("8. Eliminar nodo (Predecesor)")
        print("9. Eliminar nodo (Sucesor)")
        print("10. Recorrido por niveles")
        print("11. Altura del árbol")
        print("12. Cantidad de hojas")
        print("13. Cantidad de nodos")
        print("15. ¿Es completo?")
        print("16. ¿Es lleno?")
        print("17. Eliminar todo el árbol")
        print("0. Salir")
        op = input("Seleccione una opción: ")

        if op == "1":
            dato = int(input("Dato a insertar: "))
            arbol.insertar(dato)
        elif op == "2":
            arbol.mostrar()
        elif op == "3":
            arbol.graficar()
        elif op == "4":
            dato = int(input("Dato a buscar: "))
            print("Encontrado" if arbol.buscar(dato) else "No encontrado")
        elif op == "5":
            print("Recorrido PreOrden:")
            arbol.preOrden(arbol.raiz)
            print()
        elif op == "6":
            print("Recorrido InOrden:")
            arbol.inOrden(arbol.raiz)
            print()
        elif op == "7":
            print("Recorrido PostOrden:")
            arbol.postOrden(arbol.raiz)
            print()
        elif op == "8":
            dato = int(input("Dato a eliminar (predecesor): "))
            arbol.eliminarPredecesor(dato)
        elif op == "9":
            dato = int(input("Dato a eliminar (sucesor): "))
            arbol.eliminarSucesor(dato)
        elif op == "10":
            arbol.recorridoNiveles()
        elif op == "11":
            print("Altura del árbol:", arbol.altura())
        elif op == "12":
            print("Cantidad de hojas:", arbol.contarHojas())
        elif op == "13":
            print("Cantidad de nodos:", arbol.contarNodos())
        elif op == "15":
            print("¿Es completo?:", arbol.esCompleto())
        elif op == "16":
            print("¿Es lleno?:", arbol.esLleno())
        elif op == "17":
            arbol.eliminarArbol()
        elif op == "0":
            break
        else:
            print("Opción inválida.")
