import tkinter as tk
from tkinter import messagebox

class Utileria:
    def __init__(self, nombre, descripcion, ubicacion, cantidad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.cantidad = cantidad
        self.asignada_a_obra = False
        self.obra_actual = None

class Obra:
    def __init__(self, nombre):
        self.nombre = nombre

class Teatro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.utilerias = []

# Funciones de los botones
def agregar_utileria():
    nombre = nombre_entry.get()
    descripcion = descripcion_entry.get()
    ubicacion = ubicacion_entry.get()
    cantidad = cantidad_entry.get()
    utileria = Utileria(nombre, descripcion, ubicacion, cantidad)
    teatro.utilerias.append(utileria)
    messagebox.showinfo("Registro de utilería", "Se ha agregado la utilería correctamente.")
    actualizar_lista_utilerias()

def mostrar_utilerias():
    utilerias_text.delete(1, tk.END)
    for index, utileria in enumerate(teatro.utilerias):
        utilerias_text.insert(tk.END, f"ID: {index}\n")
        utilerias_text.insert(tk.END, f"Nombre: {utileria.nombre}\n")
        utilerias_text.insert(tk.END, f"Descripción: {utileria.descripcion}\n")
        utilerias_text.insert(tk.END, f"Teatro: {utileria.ubicacion}\n")
        utilerias_text.insert(tk.END, f"Cantidad: {utileria.cantidad}\n")
        if utileria.asignada_a_obra:
            utilerias_text.insert(tk.END, f"Asignada a la obra: {utileria.obra_actual.nombre}\n")
        utilerias_text.insert(tk.END, "-----\n")

def modificar_utileria():
    selected_item = utilerias_text.curselection()
    if selected_item:
        index = int(selected_item[0])
        utileria = teatro.utilerias[index]
        nuevo_nombre = nuevo_nombre_entry.get()
        nuevo_descripcion = nuevo_descripcion_entry.get()
        nuevo_ubicacion = nuevo_ubicacion_entry.get()
        nuevo_cantidad = nuevo_cantidad_entry.get()
        utileria.nombre = nuevo_nombre
        utileria.descripcion = nuevo_descripcion
        utileria.ubicacion = nuevo_ubicacion
        utileria.cantidad = nuevo_cantidad
        messagebox.showinfo("Modificación de utilería", "Se ha modificado la utilería correctamente.")
        actualizar_lista_utilerias()

def eliminar_utileria():
    selected_item = utilerias_text.curselection()
    if selected_item:
        index = int(selected_item[0])
        teatro.utilerias.pop(index)
        messagebox.showinfo("Eliminación de utilería", "Se ha eliminado la utilería correctamente.")
        actualizar_lista_utilerias()

def asignar_utileria():
    selected_item = utilerias_text.curselection()
    if selected_item:
        index = int(selected_item[0])
        utileria = teatro.utilerias[index]
        obra_seleccionada = obra_var.get()
        obra = Obra(obra_seleccionada)
        utileria.obra_actual = obra
        utileria.asignada_a_obra = True
        messagebox.showinfo("Asignación de utilería a obra", f"Se ha asignado la utilería a la obra '{obra_seleccionada}' correctamente.")
        actualizar_lista_utilerias()

def actualizar_lista_utilerias():
    mostrar_utilerias()
    nuevo_nombre_entry.delete(0, tk.END)
    nuevo_descripcion_entry.delete(0, tk.END)
    nuevo_ubicacion_entry.delete(0, tk.END)
    nuevo_cantidad_entry.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Registro de Utilería")

# Crear objetos de interfaz
nombre_label = tk.Label(ventana, text="Nombre:")
nombre_entry = tk.Entry(ventana)

descripcion_label = tk.Label(ventana, text="Descripción:")
descripcion_entry = tk.Entry(ventana)

ubicacion_label = tk.Label(ventana, text="Teatro:")
ubicacion_entry = tk.Entry(ventana)

cantidad_label = tk.Label(ventana, text="Cantidad:")
cantidad_entry = tk.Entry(ventana)

agregar_button = tk.Button(ventana, text="Agregar Utilería", command=agregar_utileria)

utilerias_text = tk.Listbox(ventana, width=40, height=10)

mostrar_button = tk.Button(ventana, text="Mostrar Utilerías", command=mostrar_utilerias)

nuevo_nombre_label = tk.Label(ventana, text="Nuevo Nombre:")
nuevo_nombre_entry = tk.Entry(ventana)

nuevo_descripcion_label = tk.Label(ventana, text="Nueva Descripción:")
nuevo_descripcion_entry = tk.Entry(ventana)

nuevo_ubicacion_label = tk.Label(ventana, text="Nuevo Teatro:")
nuevo_ubicacion_entry = tk.Entry(ventana)

nuevo_cantidad_label = tk.Label(ventana, text="Nueva cantidad:")
nuevo_cantidad_entry = tk.Entry(ventana)

modificar_button = tk.Button(ventana, text="Modificar Utilería", command=modificar_utileria)

eliminar_button = tk.Button(ventana, text="Eliminar Utilería", command=eliminar_utileria)

obra_label = tk.Label(ventana, text="Asignar a Obra:")
obras = ["Obra 1", "Obra 2", "Obra 3"]
obra_var = tk.StringVar(ventana)
obra_var.set(obras[0])  # Establecer valor predeterminado
obra_option_menu = tk.OptionMenu(ventana, obra_var, *obras)

asignar_obra_button = tk.Button(ventana, text="Asignar a Obra", command=asignar_utileria)


# Posicionar objetos de interfaz en la ventana
nombre_label.pack()
nombre_entry.pack()

descripcion_label.pack()
descripcion_entry.pack()

ubicacion_label.pack()
ubicacion_entry.pack()

cantidad_label.pack()
cantidad_entry.pack()

agregar_button.pack()

utilerias_text.pack()

mostrar_button.pack()

nuevo_nombre_label.pack()
nuevo_nombre_entry.pack()

nuevo_descripcion_label.pack()
nuevo_descripcion_entry.pack()

nuevo_ubicacion_label.pack()
nuevo_ubicacion_entry.pack()

nuevo_cantidad_label.pack()
nuevo_cantidad_entry.pack()

modificar_button.pack()
eliminar_button.pack()

obra_label.pack()
obra_option_menu.pack()

asignar_obra_button.pack()

# Crear teatro y ejecutar la ventana principal
teatro = Teatro("Mi Teatro")
ventana.mainloop()
