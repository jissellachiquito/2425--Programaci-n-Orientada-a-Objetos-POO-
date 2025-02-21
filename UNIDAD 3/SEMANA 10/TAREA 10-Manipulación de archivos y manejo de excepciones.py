import os
import json

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """Constructor de la clase Producto"""
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        """Convierte el objeto Producto en un diccionario para almacenamiento en archivo."""
        return {"id": self.id_producto, "nombre": self.nombre, "cantidad": self.cantidad, "precio": self.precio}

    @staticmethod
    def from_dict(data):
        """Crea un objeto Producto a partir de un diccionario."""
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# Clase Inventario
class Inventario:
    FILE_NAME = "inventario.txt"

    def __init__(self):
        """Constructor de la clase Inventario"""
        self.productos = []
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        """Guarda el inventario en un archivo."""
        try:
            with open(self.FILE_NAME, "w") as file:
                json.dump([p.to_dict() for p in self.productos], file)
        except PermissionError:
            print("Error: No tienes permiso para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar en archivo: {e}")

    def cargar_desde_archivo(self):
        """Carga el inventario desde un archivo."""
        if not os.path.exists(self.FILE_NAME):
            return
        try:
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)
                self.productos = [Producto.from_dict(p) for p in data]
        except FileNotFoundError:
            print("Archivo de inventario no encontrado, se creará uno nuevo.")
        except json.JSONDecodeError:
            print("Error: Archivo corrupto, no se pudo cargar el inventario.")
        except Exception as e:
            print(f"Error inesperado al leer el archivo: {e}")

    def agregar_producto(self, producto):
        """Añadir un nuevo producto asegurando un ID único."""
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                print("Error: ID ya existe en el inventario.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()
        print("Producto agregado con éxito.")

    def eliminar_producto(self, id_producto):
        """Eliminar producto por ID."""
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        self.guardar_en_archivo()
        print("Producto eliminado si existía.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualizar cantidad o precio de un producto por ID."""
        for p in self.productos:
            if p.id_producto == id_producto:
                if nueva_cantidad is not None:
                    p.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    p.precio = nuevo_precio
                self.guardar_en_archivo()
                print("Producto actualizado con éxito.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Buscar productos por nombre (puede haber nombres similares)."""
        return [p for p in self.productos if nombre.lower() in p.nombre.lower()]

    def mostrar_productos(self):
        """Mostrar todos los productos en el inventario."""
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos:
                print(p)


# Interfaz de usuario en la consola
def menu():
    inventario = Inventario()
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


if __name__ == "__main__":
    menu()
