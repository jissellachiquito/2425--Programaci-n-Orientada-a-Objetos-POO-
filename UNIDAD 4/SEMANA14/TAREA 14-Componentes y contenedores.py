import tkinter as tk
from tkinter import ttk, messagebox


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")  # Fondo de la ventana principal

        # Frame de entrada de datos
        self.frame_input = tk.Frame(self.root, bg="#d9d9d9", padx=10, pady=10)
        self.frame_input.pack(pady=10)

        # Etiqueta y entrada para la fecha
        tk.Label(self.frame_input, text="Fecha:", bg="#d9d9d9", font=("Georgia", 10, "bold"), fg="Blue").grid(row=0,
                                                                                                             column=0,
                                                                                                             padx=5,
                                                                                                             pady=5)
        self.entry_fecha = tk.Entry(self.frame_input, width=12, font=("Georgia", 10))
        self.entry_fecha.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta y entrada para la hora
        tk.Label(self.frame_input, text="Hora:", bg="#d9d9d9", font=("Georgia", 10, "bold"), fg="Blue").grid(row=1,
                                                                                                            column=0,
                                                                                                            padx=5,
                                                                                                            pady=5)
        self.entry_hora = tk.Entry(self.frame_input, width=15, font=("Georgia", 10))
        self.entry_hora.grid(row=1, column=1, padx=5, pady=5)

        # Etiqueta y entrada para la descripción
        tk.Label(self.frame_input, text="Descripción:", bg="#d9d9d9", font=("Georgia", 10, "bold"), fg="Blue").grid(
            row=2, column=0, padx=5, pady=5)
        self.entry_descripcion = tk.Entry(self.frame_input, width=30, font=("Georgia", 10))
        self.entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

        # Botón para agregar eventos
        self.btn_agregar = tk.Button(self.frame_input, text="Agregar Evento", command=self.agregar_evento, bg="#4caf50",
                                     fg="white", font=("Georgia", 10, "bold"))
        self.btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

        # Frame de lista de eventos
        self.frame_lista = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_lista.pack(pady=10)

        # Configuración del Treeview para mostrar eventos
        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        self.tree.column("Fecha", width=80)
        self.tree.column("Hora", width=60)
        self.tree.column("Descripción", width=250)

        self.tree.pack()

        # Botón para eliminar eventos
        self.btn_eliminar = tk.Button(self.root, text="Eliminar Evento", command=self.eliminar_evento, bg="#f44336",
                                      fg="white", font=("Georgia", 10, "bold"))
        self.btn_eliminar.pack(pady=5)

        # Botón para salir
        self.btn_salir = tk.Button(self.root, text="Salir", command=self.root.quit, bg="#2196f3", fg="white",
                                   font=("Georgia", 10, "bold"))
        self.btn_salir.pack(pady=5)

    def agregar_evento(self):
        """Función para agregar un evento a la lista."""
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_descripcion.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.entry_fecha.delete(0, tk.END)
            self.entry_hora.delete(0, tk.END)
            self.entry_descripcion.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

    def eliminar_evento(self):
        """Función para eliminar un evento seleccionado de la lista."""
        seleccionado = self.tree.selection()
        if seleccionado:
            if messagebox.askyesno("Confirmación", "¿Seguro que deseas eliminar este evento?"):
                self.tree.delete(seleccionado)
        else:
            messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

