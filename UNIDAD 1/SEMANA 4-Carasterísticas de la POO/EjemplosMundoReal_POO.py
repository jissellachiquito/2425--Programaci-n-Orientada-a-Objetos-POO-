#EJEMPLO N.-1- SISTEMA DE GESTION DE UNA TIENDA DE LIBROS
# Clase que representa un libro en la tienda
class Libro:
    def __init__(self, titulo, autor, precio):
        """Inicializa un libro con título, autor y precio"""
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def __str__(self):
        """Devuelve una representación del libro"""
        return f"{self.titulo} por {self.autor} - ${self.precio}"

# Clase que representa una tienda de libros
class Tienda:
    def __init__(self):
        """Inicializa la tienda con una lista vacía de libros"""
        self.libros = []

    def agregar_libro(self, libro):
        """Añade un libro a la tienda"""
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la tienda.")

    def mostrar_libros(self):
        """Muestra todos los libros disponibles en la tienda"""
        if self.libros:
            print("Libros disponibles:")
            for libro in self.libros:
                print(libro)
        else:
            print("No hay libros disponibles en la tienda.")

# Ejemplo de uso
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 15)
libro2 = Libro("1984", "George Orwell", 12)

tienda = Tienda()
tienda.agregar_libro(libro1)
tienda.agregar_libro(libro2)

tienda.mostrar_libros()

#EJEMPLO N.-2-RESERVACION EN UN HOTEL
#Clase que representa una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo):
        """
        Inicializa una habitación con su número y tipo (individual o doble).
        """
        self.numero = numero
        self.tipo = tipo
        self.ocupada = False  # Inicialmente, la habitación está libre

    def ocupar(self):
        """Marca la habitación como ocupada"""
        if not self.ocupada:
            self.ocupada = True
            print(f"La habitación {self.numero} ahora está ocupada.")
        else:
            print(f"La habitación {self.numero} ya está ocupada.")

    def liberar(self):
        """Marca la habitación como libre"""
        if self.ocupada:
            self.ocupada = False
            print(f"La habitación {self.numero} ahora está libre.")
        else:
            print(f"La habitación {self.numero} ya está libre.")

# Clase que representa a un cliente
class Cliente:
    def __init__(self, nombre):
        """
        Inicializa un cliente con su nombre.
        """
        self.nombre = nombre
        self.reserva = None  # El cliente no tiene una reserva al principio

    def hacer_reserva(self, habitacion):
        """El cliente intenta reservar una habitación"""
        if not habitacion.ocupada:
            habitacion.ocupar()
            self.reserva = habitacion
            print(f"{self.nombre} ha reservado la habitación {habitacion.numero}.")
        else:
            print(f"La habitación {habitacion.numero} ya está ocupada. No se puede reservar.")

    def cancelar_reserva(self):
        """El cliente cancela su reserva"""
        if self.reserva:
            self.reserva.liberar()
            print(f"{self.nombre} ha cancelado su reserva para la habitación {self.reserva.numero}.")
            self.reserva = None
        else:
            print(f"{self.nombre} no tiene ninguna reserva para cancelar.")

# Ejemplo de uso
habitacion1 = Habitacion(101, "Individual")
habitacion2 = Habitacion(102, "Doble")

cliente1 = Cliente("Juan Pérez")
cliente2 = Cliente("Ana Gómez")

# El cliente 1 hace una reserva
cliente1.hacer_reserva(habitacion1)

# El cliente 2 intenta reservar la misma habitación
cliente2.hacer_reserva(habitacion1)

# El cliente 1 cancela su reserva
cliente1.cancelar_reserva()

# El cliente 2 ahora puede reservar la habitación
cliente2.hacer_reserva(habitacion1)
