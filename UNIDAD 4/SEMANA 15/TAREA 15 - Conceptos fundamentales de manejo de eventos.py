import tkinter as tk
from idlelib.configdialog import font_sample_text
from tkinter import messagebox

# funcion para anadir tarea
def añadir_tarea():
    tarea = entrada.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

# funcion para marcar una tarea completada
def marcar_completada():
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(tarea_seleccionada)
        lista_tareas.delete(tarea_seleccionada)
        lista_tareas.insert(tarea_seleccionada, f"{tarea} (Completada)")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

# funcion para eliminar tarea
def eliminar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()[0]
        lista_tareas.delete(tarea_seleccionada)   #Elimina la tarea seleccionada
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.") #muestra una advertencia si no se seleccionó ninguna tarea

 # función para añadir una tarea cuando se presiona "Enter"
def manejar_enter(event):
    añadir_tarea()

# configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas", )
ventana.geometry("350x350")

# campo de entrada para escribir nuevas tareas
entrada = tk.Entry(ventana, width=30)
entrada.grid(row=0, column=0, padx=10, pady=10, )
# Vincula la tecla "Enter" a la función manejar_enter
entrada.bind("<Return>", manejar_enter)

# Botón para añadir tareas
boton_añadir = tk.Button(ventana, text="Añadir Tarea", command=añadir_tarea,)
boton_añadir.grid(row=0, column=1, padx=10, pady=10, )

# Botón para marcar una tarea como completada
boton_completada = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
boton_completada.grid(row=1, column=0, padx=10, pady=10)

# botón para eliminar una tarea
boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.grid(row=1, column=1, padx=10, pady=10)

# listbox para mostrar las tareas actuales
lista_tareas = tk.Listbox(ventana, width=50, height=10)
lista_tareas.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# vincular atajos de teclado
ventana.bind("<a>", lambda event: añadir_tarea())  # Ctrl + A para añadir tarea
ventana.bind("<m>", lambda event: marcar_completada())  # Ctrl + M para marcar como completada
ventana.bind("<d>", lambda event: eliminar_tarea())  # Ctrl + D para eliminar tarea

# ejecutar la aplicación
ventana.mainloop()