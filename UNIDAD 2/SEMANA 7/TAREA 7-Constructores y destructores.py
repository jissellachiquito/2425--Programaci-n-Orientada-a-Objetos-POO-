# EJEMPLO DE GESTION DE ARCHIVO DE UN TEXTO
# Clase que gestiona un archivo de texto
class GestorArchivo:
    # constructor: inicializa el archivo y lo abre para escritura
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        print(f"Creando el archivo: {self.nombre_archivo}")
        self.archivo = open(self.nombre_archivo, 'w')  # abre el archivo para escribir

    # método para escribir en el archivo
    def escribir(self, texto):
        if self.archivo:  # verifica que el archivo esté abierto
            self.archivo.write(texto + '\n')
            print(f"Escrito en {self.nombre_archivo}: {texto}")
        else:
            print("El archivo no está disponible para escribir.")

    # destructor: cierra el archivo si aún está abierto
    def __del__(self):
        if self.archivo:
            self.archivo.close()
            print(f"El archivo {self.nombre_archivo} ha sido cerrado correctamente.")
        print(f"El objeto de gestión del archivo '{self.nombre_archivo}' ha sido eliminado.")


# programa principal
if __name__ == "__main__":
    print("Inicio del programa")

    #crear un objeto de la clase
    gestor = GestorArchivo("mi_archivo.txt")

    #escribir contenido en el archivo
    gestor.escribir("Hola, este es un ejemplo de escritura.")
    gestor.escribir("Este es otro mensaje en el archivo.")

    #el objeto se eliminará automáticamente al finalizar el programa
    print("Fin del programa")
