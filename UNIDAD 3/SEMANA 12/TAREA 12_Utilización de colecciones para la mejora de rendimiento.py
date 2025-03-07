class Libro:
    """Representa un libro en la biblioteca."""
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (autor, titulo)  # se almacena como tupla porque es inmutable
        self.categoria = categoria
        self.isbn = isbn  # identificador único del libro

    def __str__(self):
        return f"{self.info[1]} por {self.info[0]} (Categoría: {self.categoria}, ISBN: {self.isbn})"

class Usuario:
    """Representa un usuario de la biblioteca."""
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id  # identificador único del usuario
        self.libros_prestados = []  # lista de libros prestados al usuario

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"

class Biblioteca:
    """Sistema de gestión de la biblioteca."""
    def __init__(self):
        self.libros = {}  # diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # diccionario con ID de usuario como clave y objeto Usuario como valor

    def agregar_libro(self, libro):
        """Añade un libro a la biblioteca si no existe ya."""
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("El libro ya está en la biblioteca.")

    def quitar_libro(self, isbn):
        """Elimina un libro de la biblioteca si existe."""
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado correctamente.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        """Registra un nuevo usuario en la biblioteca si no existe."""
        if usuario.user_id not in self.usuarios:
            self.usuarios[usuario.user_id] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")

    def dar_baja_usuario(self, user_id):
        """Elimina un usuario de la biblioteca si existe."""
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            print("Usuario eliminado correctamente.")
        else:
            print("El usuario no existe.")

    def prestar_libro(self, user_id, isbn):
        """Presta un libro a un usuario si está disponible en la biblioteca."""
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[user_id]
            libro = self.libros.pop(isbn)  # se retira del catálogo de libros disponibles
            usuario.libros_prestados.append(libro)  # se añade a la lista de libros prestados del usuario
            print(f"Libro prestado a {usuario.nombre}: {libro}")
        else:
            print("No se puede prestar el libro: usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        """Permite a un usuario devolver un libro y lo reintegra al catálogo."""
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro  # se regresa al catálogo de la biblioteca
                    print(f"Libro devuelto: {libro}")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        """Busca libros en la biblioteca según título, autor o categoría."""
        resultados = [libro for libro in self.libros.values() if getattr(libro, criterio) == valor]
        if resultados:
            print("Libros encontrados:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

    def listar_libros_prestados(self, user_id):
        """Muestra los libros prestados a un usuario específico."""
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")

# Ejemplo de uso del sistema de biblioteca
biblioteca = Biblioteca()
libro1 = Libro("Orgullo y prejuicio", "Jane Austen", "Romance", "101222333")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", "444555666")
usuario1 = Usuario("Alejandra López", "U042")

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar un usuario
biblioteca.registrar_usuario(usuario1)

# Prestar un libro al usuario
biblioteca.prestar_libro("U002", "111222333")

# Listar libros prestados al usuario
biblioteca.listar_libros_prestados("U002")
