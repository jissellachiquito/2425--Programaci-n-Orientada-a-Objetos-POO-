import json


class Producto:
    """
    Clase que representa un producto en el inventario.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible
        self.precio = precio  # Precio del producto

    def actualizar_cantidad(self, nueva_cantidad):
        """Actualiza la cantidad del producto."""
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del producto."""
        self.precio = nuevo_precio

    def to_dict(self):
        """Convierte el objeto Producto a un diccionario para facilitar su almacenamiento en un archivo."""
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


class Inventario:
    """
    Clase que gestiona el inventario de productos.
    """

    def __init__(self):
        self.productos = {}  # Diccionario para almacenar los productos con el ID como clave

    def agregar_producto(self, producto):
        """Añade un nuevo producto al inventario."""
        if producto.id_producto in self.productos:
            print("El ID del producto ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario por su ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("El producto con ese ID no existe.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad y/o precio de un producto."""
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].actualizar_precio(precio)
            print("Producto actualizado correctamente.")
        else:
            print("El producto con ese ID no existe.")

    def buscar_producto(self, nombre):
        """Busca y muestra productos por nombre."""
        encontrados = [p.to_dict() for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if self.productos:
            for producto in self.productos.values():
                print(producto.to_dict())
        else:
            print("El inventario está vacío.")

    def guardar_en_archivo(self, archivo):
        """Guarda el inventario en un archivo JSON."""
        with open(archivo, "w") as f:
            json.dump({id_prod: prod.to_dict() for id_prod, prod in self.productos.items()}, f)
        print("Inventario guardado correctamente.")

    def cargar_desde_archivo(self, archivo):
        """Carga el inventario desde un archivo JSON."""
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                self.productos = {id_prod: Producto(**prod) for id_prod, prod in datos.items()}
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("Archivo no encontrado. Se iniciará un inventario vacío.")


# Función para mostrar el menú interactivo
def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo("inventario.json")

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Nuevo precio (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == "5":
            inventario.mostrar_productos()
        elif opcion == "6":
            inventario.guardar_en_archivo("inventario.json")
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Ejecutar el menú si el script se ejecuta directamente
if __name__ == "__main__":
    menu()

