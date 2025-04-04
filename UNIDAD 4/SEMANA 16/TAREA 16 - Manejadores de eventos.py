import tkinter as tk
from tkinter import messagebox

#función para añadir una nueva tarea
def agregar_tarea(event=None):
    tarea = entrada.get()  #obtener texto de la entrada
    if tarea:  #verifica que no esté vacío
        lista_tareas.insert(tk.END, tarea)  #agrega la tarea al final de la lista
        entrada.delete(0, tk.END)  #limpia el campo de entrada
    else:
        messagebox.showwarning("Aviso", "Por favor, ingresa una tarea.")

#función para marcar una tarea como completada
def completar_tarea(event=None):
    try:
        index = lista_tareas.curselection()[0]  #obtener índice de la tarea seleccionada
        tarea = lista_tareas.get(index)  #obtener el texto de la tarea
        if not tarea.startswith("[✔]"):  #evita marcar dos veces
            lista_tareas.delete(index)
            lista_tareas.insert(index, f"[✔] {tarea}")  #marca con ✔
    except IndexError:
        messagebox.showinfo("Info", "Selecciona una tarea para completar.")

#función para eliminar una tarea seleccionada
def eliminar_tarea(event=None):
    try:
        index = lista_tareas.curselection()[0]  #obtener índice de la tarea
        lista_tareas.delete(index)  #eliminar la tarea
    except IndexError:
        messagebox.showinfo("Info", "Selecciona una tarea para eliminar.")

#función para cerrar la aplicación con la tecla Escape
def cerrar_aplicacion(event=None):
    ventana.destroy()  #cierra la ventana

#crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("400x400")
ventana.configure(bg="#f0f4f7")


#campo de entrada para escribir la tarea
entrada = tk.Entry(ventana, font=("Georgia", 14))
entrada.pack(pady=10)
entrada.focus_set()  #coloca el cursor en el campo al iniciar

#botones para agregar, completar y eliminar tareas
boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea, bg="lightgreen" )
boton_agregar.pack(pady=5)

boton_completar = tk.Button(ventana, text="Completar Tarea", command=completar_tarea,bg="lightgreen")
boton_completar.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea,bg="lightgreen")
boton_eliminar.pack(pady=5)

#lista de tareas
lista_tareas = tk.Listbox(ventana, font=("Georgia", 12), width=40, height=10)
lista_tareas.pack(pady=10)

#atajos de teclado
ventana.bind('<Return>', agregar_tarea)       # Enter para agregar tarea
ventana.bind('<c>', completar_tarea)          # C para completar
ventana.bind('<C>', completar_tarea)          # C mayúscula también
ventana.bind('<d>', eliminar_tarea)           # D para eliminar
ventana.bind('<D>', eliminar_tarea)           # D mayúscula también
ventana.bind('<Delete>', eliminar_tarea)      # Tecla Delete para eliminar
ventana.bind('<Escape>', cerrar_aplicacion)   # Escape para cerrar la app

#iniciar bucle de la aplicación
ventana.mainloop()
