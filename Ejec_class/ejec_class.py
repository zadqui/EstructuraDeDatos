import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# -----------------------
# Clase lógica de la Pila
# -----------------------
class Pila:
    def __init__(self):
        self.items = []
    def apilar(self, elemento): self.items.append(elemento)
    def desapilar(self): return self.items.pop() if not self.esta_vacia() else None
    def cima(self): return self.items[-1] if not self.esta_vacia() else None
    def esta_vacia(self): return len(self.items) == 0
    def limpiar(self): self.items.clear()
    def __len__(self): return len(self.items)

# -----------------------
# Interfaz Gráfica
# -----------------------
class MultiPilaGUI:
    def __init__(self, master):
        self.master = master
        master.title("📦 Visualizador de Pilas (Cima Arriba)")
        master.geometry("1150x750")
        master.configure(bg="#ecf0f1")

        # Tema visual
        self.style = ttk.Style(master)
        self.style.theme_use('clam')

        # Personalización de estilo
        self.style.configure("TFrame", background="#ecf0f1")
        self.style.configure("TLabelframe", background="#ecf0f1", font=("Segoe UI", 10, "bold"))
        self.style.configure("TLabel", background="#ecf0f1", font=("Segoe UI", 10))
        self.style.configure("TButton", font=("Segoe UI", 9, "bold"), padding=6)
        self.style.configure("TEntry", padding=4)

        self.pilas = {}
        self.pila_counter = 0

        # --- Panel lateral (controles) ---
        self.control_panel = ttk.Frame(master, width=300)
        self.control_panel.pack(side=tk.LEFT, fill=tk.Y, padx=15, pady=15)
        self.control_panel.pack_propagate(False)

        # --- Área de visualización (canvas) ---
        canvas_frame = ttk.Frame(master)
        canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.canvas = tk.Canvas(canvas_frame, bg="#ffffff", highlightthickness=1, highlightbackground="#bdc3c7")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.status_bar = ttk.Label(canvas_frame, text="✨ Bienvenido al visualizador de pilas.", 
                                    anchor=tk.W, font=("Segoe UI", 9, "italic"))
        self.status_bar.pack(fill=tk.X, pady=(5,0))

        # Construcción de paneles
        self.setup_control_panel()

        # Inicializar
        self.actualizar_controles()
        self.dibujar_canvas()

    # -----------------------
    # Panel lateral
    # -----------------------
    def setup_control_panel(self):
        # 1. Gestión de Pilas
        gestion_frame = ttk.LabelFrame(self.control_panel, text="⚙️ Gestión de Pilas")
        gestion_frame.pack(fill=tk.X, pady=10)

        self.listbox_pilas = tk.Listbox(gestion_frame, height=8, exportselection=False, 
                                        font=("Segoe UI", 9), bg="#fdfefe", relief="solid", borderwidth=1)
        self.listbox_pilas.pack(fill=tk.X, padx=5, pady=5)
        self.listbox_pilas.bind('<<ListboxSelect>>', self.actualizar_controles)
        self.listbox_pilas.bind('<Double-1>', self.renombrar_pila)

        ttk.Button(gestion_frame, text="➕ Crear Nueva Pila", command=self.crear_pila).pack(fill=tk.X, padx=5, pady=3)
        ttk.Button(gestion_frame, text="🗑️ Eliminar Pila", command=self.eliminar_pila).pack(fill=tk.X, padx=5, pady=3)

        # 2. Operaciones
        ops_frame = ttk.LabelFrame(self.control_panel, text="📌 Operaciones")
        ops_frame.pack(fill=tk.X, pady=10)

        ttk.Label(ops_frame, text="Elemento:").pack(padx=5)
        self.entry_elemento = ttk.Entry(ops_frame, font=("Segoe UI", 9))
        self.entry_elemento.pack(fill=tk.X, padx=5, pady=5)
        self.entry_elemento.bind("<Return>", lambda e: self.apilar())

        self.btn_apilar = ttk.Button(ops_frame, text="⬆️ Apilar (Push)", command=self.apilar)
        self.btn_apilar.pack(fill=tk.X, padx=5, pady=3)
        self.btn_desapilar = ttk.Button(ops_frame, text="⬇️ Desapilar (Pop)", command=self.desapilar)
        self.btn_desapilar.pack(fill=tk.X, padx=5, pady=3)
        self.btn_cima = ttk.Button(ops_frame, text="👀 Ver Cima (Peek)", command=self.ver_cima)
        self.btn_cima.pack(fill=tk.X, padx=5, pady=3)
        self.btn_limpiar = ttk.Button(ops_frame, text="🧹 Limpiar Pila", command=self.limpiar_pila_seleccionada)
        self.btn_limpiar.pack(fill=tk.X, padx=5, pady=3)

        # 3. Información
        info_frame = ttk.LabelFrame(self.control_panel, text="ℹ️ Información")
        info_frame.pack(fill=tk.X, pady=10)
        self.info_label = ttk.Label(info_frame, text="Seleccione una pila.", wraplength=260, font=("Segoe UI", 9))
        self.info_label.pack(padx=5, pady=5)

    # -----------------------
    # Métodos auxiliares
    # -----------------------
    def mostrar_mensaje_status(self, msg, duration=3000):
        self.status_bar.config(text=msg)
        if duration:
            self.master.after(duration, lambda: self.status_bar.config(text="✨ Listo."))

    def obtener_pila_seleccionada(self):
        try:
            indice = self.listbox_pilas.curselection()[0]
            nombre_pila = self.listbox_pilas.get(indice)
            return nombre_pila, self.pilas[nombre_pila]
        except IndexError:
            return None, None

    # -----------------------
    # CRUD de Pilas
    # -----------------------
    def crear_pila(self):
        self.pila_counter += 1
        nombre_pila = f"Pila-{self.pila_counter}"
        self.pilas[nombre_pila] = Pila()
        self.listbox_pilas.insert(tk.END, nombre_pila)
        self.listbox_pilas.selection_clear(0, tk.END)
        self.listbox_pilas.selection_set(tk.END)
        self.actualizar_controles()
        self.dibujar_canvas()
        self.mostrar_mensaje_status(f"✅ Pila '{nombre_pila}' creada.")

    def eliminar_pila(self):
        nombre_pila, _ = self.obtener_pila_seleccionada()
        if nombre_pila and messagebox.askyesno("Confirmar", f"¿Eliminar '{nombre_pila}'?"):
            del self.pilas[nombre_pila]
            self.listbox_pilas.delete(tk.ACTIVE)
            self.actualizar_controles()
            self.dibujar_canvas()
            self.mostrar_mensaje_status(f"🗑️ Pila '{nombre_pila}' eliminada.")

    def renombrar_pila(self, event):
        nombre_pila_viejo, pila = self.obtener_pila_seleccionada()
        if not nombre_pila_viejo: return
        nuevo_nombre = simpledialog.askstring("Renombrar", "Introduce el nuevo nombre:", initialvalue=nombre_pila_viejo)
        if nuevo_nombre and nuevo_nombre != nombre_pila_viejo and nuevo_nombre not in self.pilas:
            indice = self.listbox_pilas.curselection()[0]
            self.pilas[nuevo_nombre] = self.pilas.pop(nombre_pila_viejo)
            self.listbox_pilas.delete(indice)
            self.listbox_pilas.insert(indice, nuevo_nombre)
            self.listbox_pilas.selection_set(indice)
            self.dibujar_canvas()
            self.actualizar_controles()
            self.mostrar_mensaje_status(f"✏️ Pila renombrada a '{nuevo_nombre}'.")

    # -----------------------
    # Controles de botones
    # -----------------------
    def limpiar_pila_seleccionada(self):
        nombre_pila, pila = self.obtener_pila_seleccionada()
        if pila and not pila.esta_vacia():
            if messagebox.askyesno("Confirmar", f"Vaciar '{nombre_pila}'?"):
                pila.limpiar()
                self.actualizar_controles()
                self.dibujar_canvas()
                self.mostrar_mensaje_status(f"🧹 Pila '{nombre_pila}' vaciada.")

    def actualizar_controles(self, event=None):
        nombre, pila = self.obtener_pila_seleccionada()
        estado_activo = tk.NORMAL if pila else tk.DISABLED
        estado_vacio = tk.DISABLED if not pila or pila.esta_vacia() else tk.NORMAL
        self.btn_apilar.config(state=estado_activo)
        self.btn_desapilar.config(state=estado_vacio)
        self.btn_cima.config(state=estado_vacio)
        self.btn_limpiar.config(state=estado_vacio)
        if pila: self.info_label.config(text=f"Pila: '{nombre}'\nElementos: {len(pila)}")
        else: self.info_label.config(text="Seleccione o cree una pila.")

    # -----------------------
    # Dibujar en Canvas
    # -----------------------
    def dibujar_canvas(self):
        self.canvas.delete("all")
        if not self.pilas:
            self.canvas.create_text(self.canvas.winfo_width()/2, self.canvas.winfo_height()/2, 
                                    text="Crea una pila para comenzar", font=("Segoe UI", 14, "italic"), fill="grey")
            return
            
        total_pilas, canvas_w = len(self.pilas), self.canvas.winfo_width()
        
        for i, (nombre, pila) in enumerate(self.pilas.items()):
            x_centro = (canvas_w / (total_pilas + 1)) * (i + 1)
            y_inicio = 60 # margen superior
            
            self.canvas.create_text(x_centro, 30, text=nombre, font=("Segoe UI", 11, "bold"), fill="#2c3e50")
            
            if pila.esta_vacia():
                self.canvas.create_text(x_centro, y_inicio, text="(Vacía)", font=("Segoe UI", 10, "italic"), fill="grey")
                continue

            elementos_invertidos = reversed(list(enumerate(pila.items)))

            for j_inv, (j, elemento) in enumerate(elementos_invertidos):
                y1 = y_inicio + (j_inv * 45)
                y2 = y1 + 40
                
                rect_tag = f"rect_{nombre}_{j}"
                text_tag = f"text_{nombre}_{j}"
                
                self.canvas.create_rectangle(x_centro-65, y1, x_centro+65, y2, 
                                             fill="#3498db", outline="#2c3e50", width=2, tags=rect_tag)
                self.canvas.create_text(x_centro, y1 + 20, text=elemento, 
                                        font=("Segoe UI", 10, "bold"), fill="white", tags=text_tag)
                
                if j_inv == 0:
                     self.canvas.create_text(x_centro + 85, y1 + 20, text="⬅ Cima", fill="red", font=("Segoe UI", 9, "bold"))

# -----------------------
# Ejecución principal
# -----------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = MultiPilaGUI(root)
    root.mainloop()