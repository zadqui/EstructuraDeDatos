class ColaDeImpresion:
    def __init__(self):
        """
        Constructor: Se ejecuta al crear una nueva cola.
        Inicializa una lista vacía para guardar las tareas.
        """
        self.tareas = []
        print(" 📠 Impresora lista para recibir trabajos.\n")

    def vacia(self):
        """Devuelve True si la cola está vacía, False en caso contrario."""
        return len(self.tareas) == 0

    def encolar(self, tarea):
        """
        Agrega una nueva tarea al final de la cola.
        """
        self.tareas.append(tarea)
        print(f" ✅ Documento recibido: '{tarea}'.")
        self.mostrar_cola()

    def procesar(self):
        """
        Método (Desencolar): Imprime (elimina) el primer documento de la cola.
        """
        if self.vacia():
            print(" ⚠️ No hay tareas en la cola.\n")
        else:
            # .pop(0) elimina el elemento en el índice 0 (el primero).
            tarea_actual = self.tareas.pop(0)
            print(f" 🔄 Imprimiendo: '{tarea_actual}'...")
            self.mostrar_cola()

    def mostrar_cola(self):
        """Método auxiliar para mostrar el estado actual de la cola."""
        if self.vacia():
            print("   (Cola vacía)\n")
        else:
            print(f"   Cola actual: {self.tareas}\n")


# Ejemplo de uso
impresora = ColaDeImpresion()

# Se agregan documentos a la cola
impresora.encolar("Informe_Mensual.docx")
impresora.encolar("Grafico_Estadistico.png")
impresora.encolar("Reporte_Financiero.pdf")

# Se procesan algunos documentos
impresora.procesar()
impresora.procesar()

# Se agrega otro documento
impresora.encolar("Diapositivas_Clase.pptx")

# Se procesan los documentos restantes
impresora.procesar()
impresora.procesar()
impresora.procesar()
