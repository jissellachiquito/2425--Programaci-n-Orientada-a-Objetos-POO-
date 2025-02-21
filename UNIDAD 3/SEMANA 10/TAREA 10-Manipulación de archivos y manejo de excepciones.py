import os
import json

# Clase que representa un producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Constructor de la clase Producto"""
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad en stock
        self.precio = precio  # Precio del producto

    def to_dict(self):
        """Convierte el producto a un diccionario para su almacenamiento en archivo"""
        return {"id": self.id_producto, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

    @staticmethod
    def from_dict(data):
        """Crea un objeto Producto a partir de un diccionario"""
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# Clase que representa el inventario de la tienda
class Inventario:
    FILE_NAME = "inventario.txt"  # Archivo para almacenar el inventario

    def __init__(self):
        """Constructor de la clase Inventario"""
        self.productos = []  # Lista de productos en el inventario
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        """Guarda los productos en un archivo JSON manejando excepciones"""
        try:
            with open(self.FILE_NAME, "w") as f:
                json.dump([p.to_dict() for p in self.productos], f)
            print("Inventario guardado correctamente en archivo.")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar el archivo: {e}")

    def cargar_desde_archivo(self):
        """Carga los productos desde un archivo JSON manejando excepciones"""
        if not os.path.exists(self.FILE_NAME):
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
            return
        try:
            with open(self.FILE_NAME, "r") as f:
                datos = json.load(f)
                self.productos = [Producto.from_dict(p) for p in datos]
            print("Inventario cargado correctamente desde archivo.")
        except FileNotFoundError:
            print("Error: Archivo de inventario no encontrado.")
        except json.JSONDecodeError:
            print("Error: Archivo de inventario corrupto.")
        except Exception as e:
            print(f"Error inesperado al cargar el archivo: {e}")
    # Añade un producto al inventario
    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: ID ya existe en el inventario.")
            return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado con éxito.")

    # Elimina un producto por su ID
    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        self.guardar_en_archivo()
        print("Producto eliminado si existía.")

    # Actualiza la cantidad o el precio de un producto por su ID
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                self.guardar_en_archivo()
                print("Producto actualizado con éxito.")
                return
        print("Error: Producto no encontrado.")

    # Busca productos por nombre
    def buscar_producto(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
    # Muestra todos los productos en el inventario
    def mostrar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos:
                print(p)

# Función para mostrar el menú y gestionar las opciones del usuario
def menu():
    inventario = Inventario() # Interfaz de usuario en la consola
    while True:
        print("\n--- MENÚ DE GESTIÓN DE INVENTARIO ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID único del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese nueva cantidad (Enter para omitir): ")
            nuevo_precio = input("Ingrese nuevo precio (Enter para omitir): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")
# Punto de entrada del programa
if __name__ == "__main__":
    menu()


