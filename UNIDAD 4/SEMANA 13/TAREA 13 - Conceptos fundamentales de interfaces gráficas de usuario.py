import tkinter as tk
from tkinter import messagebox


def agregar_elemento():
    texto = entrada_texto.get()
    if texto:
        lista_datos.insert(tk.END, texto)
        entrada_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

def limpiar_lista():
    lista_datos.delete(0, tk.END)


# configuración de la ventana principal
root = tk.Tk()
root.title("Aplicación Básica sobre GUI")
root.geometry("500x500")
root.configure(bg="lightgreen")

# etiqueta y campo de entrada
tk.Label(root, text="Ingrese un dato:", font="georgia").pack(pady=5)
entrada_texto = tk.Entry(root, width=40)
entrada_texto.pack(pady=5)

# boton para agregar elementos
boton_agregar = tk.Button(root, text="AGREGAR",background="cyan",font="georgia", command=agregar_elemento)
boton_agregar.pack(pady=5)

# lista para mostrar datos
lista_datos = tk.Listbox(root, width=50, height=10)
lista_datos.pack(pady=5)

# boton para limpiar toda la lista
boton_limpiar_lista = tk.Button(root, text="Limpiar Lista",font="georgia", command=limpiar_lista)
boton_limpiar_lista.pack(pady=5)

# ejecutar la aplicación
root.mainloop()


