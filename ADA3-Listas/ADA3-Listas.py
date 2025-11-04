class NodoIngrediente:
    """Nodo para la lista enlazada de ingredientes"""
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


class Postre:
    """Representa un postre con su lista enlazada de ingredientes"""
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = None  # cabeza de la lista de ingredientes


class GestorPostres:
    """Maneja todos los postres (lista principal)"""
    def __init__(self):
        self.postres = []  # lista principal (arreglo de postres)

    # [a] Mostrar ingredientes de un postre
    def mostrar_ingredientes(self, nombre_postre):
        postre = self.buscar_postre(nombre_postre)
        if postre:
            print(f"\nIngredientes de {nombre_postre}:")
            actual = postre.ingredientes
            if not actual:
                print("  (sin ingredientes)")
                return
            while actual:
                print(f"  - {actual.nombre}")
                actual = actual.siguiente
        else:
            print(f"❌ El postre '{nombre_postre}' no existe.")

    # [b] Insertar nuevo ingrediente
    def agregar_ingrediente(self, nombre_postre, ingrediente):
        postre = self.buscar_postre(nombre_postre)
        if not postre:
            print(f"❌ El postre '{nombre_postre}' no existe.")
            return

        nuevo = NodoIngrediente(ingrediente)
        if not postre.ingredientes:
            postre.ingredientes = nuevo
        else:
            actual = postre.ingredientes
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        print(f"✅ Ingrediente '{ingrediente}' agregado a '{nombre_postre}'.")

    # [c] Eliminar un ingrediente
    def eliminar_ingrediente(self, nombre_postre, ingrediente):
        postre = self.buscar_postre(nombre_postre)
        if not postre:
            print(f"❌ El postre '{nombre_postre}' no existe.")
            return

        actual = postre.ingredientes
        anterior = None
        while actual and actual.nombre != ingrediente:
            anterior = actual
            actual = actual.siguiente

        if not actual:
            print(f"❌ El ingrediente '{ingrediente}' no se encontró en '{nombre_postre}'.")
            return

        if anterior is None:
            postre.ingredientes = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente

        print(f"🗑️ Ingrediente '{ingrediente}' eliminado de '{nombre_postre}'.")

    # [d] Alta de un postre
    def agregar_postre(self, nombre, lista_ingredientes):
        if self.buscar_postre(nombre):
            print(f"⚠️ El postre '{nombre}' ya existe.")
            return
        nuevo_postre = Postre(nombre)
        for ing in lista_ingredientes:
            self.agregar_ingrediente_a_postre(nuevo_postre, ing)
        self.postres.append(nuevo_postre)
        self.postres.sort(key=lambda p: p.nombre.lower())
        print(f"🍰 Postre '{nombre}' agregado con sus ingredientes.")

    def agregar_ingrediente_a_postre(self, postre, nombre_ing):
        nuevo = NodoIngrediente(nombre_ing)
        if not postre.ingredientes:
            postre.ingredientes = nuevo
        else:
            actual = postre.ingredientes
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # [e] Baja de un postre
    def eliminar_postre(self, nombre):
        for i, p in enumerate(self.postres):
            if p.nombre.lower() == nombre.lower():
                del self.postres[i]
                print(f"🗑️ Postre '{nombre}' eliminado.")
                return
        print(f"❌ El postre '{nombre}' no existe.")

    # Buscar postre auxiliar
    def buscar_postre(self, nombre):
        for p in self.postres:
            if p.nombre.lower() == nombre.lower():
                return p
        return None

    # [2] Eliminar postres repetidos
    def eliminar_repetidos(self):
        nombres_vistos = set()
        nuevos = []
        for p in self.postres:
            if p.nombre.lower() not in nombres_vistos:
                nombres_vistos.add(p.nombre.lower())
                nuevos.append(p)
        self.postres = nuevos
        print("♻️ Postres repetidos eliminados correctamente.")

    # Mostrar todos los postres
    def mostrar_postres(self):
        if not self.postres:
            print("📂 No hay postres registrados.")
            return
        print("\nLISTA DE POSTRES:")
        for p in self.postres:
            print(f"🍮 {p.nombre}")
