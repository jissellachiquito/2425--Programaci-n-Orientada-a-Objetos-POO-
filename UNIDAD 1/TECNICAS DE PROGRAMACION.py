# EJEMPLO DE ABSTRACCION
# define la estructura básica de un vehículo
from abc import ABC, abstractmethod
class Vehiculo(ABC):
    abstractmethod
    def encender(self):
        pass

    abstractmethod
    def apagar(self):
        pass

    abstractmethod
    def acelerar(self):
        pass

# clase  para un automóvil
class Automovil(Vehiculo):
    def encender(self):
        return "El automóvil está encendido."

    def apagar(self):
        return "El automóvil está apagado."

    def acelerar(self):
        return "El automóvil está acelerando a 60 km/h."

# clase  para una motocicleta
class Motocicleta(Vehiculo):
    def encender(self):
        return "La motocicleta está encendida."

    def apagar(self):
        return "La motocicleta está apagada."

    def acelerar(self):
        return "La motocicleta está acelerando a 80 km/h."

# clase  para un camión
class Camion(Vehiculo):
    def encender(self):
        return "El camión está encendido."

    def apagar(self):
        return "El camión está apagado."

    def acelerar(self):
        return "El camión está acelerando a 40 km/h."

# Uso de cada una de las clases
vehiculos = [Automovil(), Motocicleta(), Camion()]

for vehiculo in vehiculos:
    print(vehiculo.encender())
    print(vehiculo.acelerar())
    print(vehiculo.apagar())
    print("-" * 40)  # Separador entre vehículos


# EJEMPLO DE ENCAPSULACION
# define una clase de estudiante que protege el atributo edad
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad  # atributo privado

    # método para modificar la edad, con validación
    def establecer_edad(self, edad):
        if 0 < edad < 120:  # validación la edad debe estar en un rango razonable
            self.__edad = edad
        else:
            print("Edad no válida")

    # método para acceder a la edad
    def obtener_edad(self):
        return self.__edad

# Uso de la clase
estudiante = Estudiante("María", 20)
print(estudiante.obtener_edad())  # muestra la edad inicial
estudiante.establecer_edad(25)    # cambia la edad
print(estudiante.obtener_edad())  # muestra la edad actualizada
estudiante.establecer_edad(130)   # intento fallido de asignar una edad no válida

# EJEMPLO DE HERENCIA
# crear una estructura jerárquica de empleados

# clase base para empleados
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    # método común para mostrar detalles del empleado
    def detalles(self):
        return f"Empleado: {self.nombre}, Salario: ${self.salario}"

# subclase para gerentes que hereda de Empleado
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)  # Llama al constructor de la clase base
        self.departamento = departamento

    #   método para incluir información adicional
    def detalles(self):
        return f"Gerente: {self.nombre}, Salario: ${self.salario}, Departamento: {self.departamento}"

# subclase para pasantes que hereda de Empleado
class Pasante(Empleado):
    def __init__(self, nombre, salario, duracion):
        super().__init__(nombre, salario)
        self.duracion = duracion  # Duración de la pasantía en meses

    def detalles(self):
        return f"Pasante: {self.nombre}, Salario: ${self.salario}, Duración: {self.duracion} meses"

# uso de las clases
empleados = [
    Empleado("Luis", 3000),       # Instancia de la clase base
    Gerente("Ana", 5000, "IT"),  # Instancia de la subclase Gerente
    Pasante("Pedro", 1000, 6)    # Instancia de la subclase Pasante
]

for empleado in empleados:
    print(empleado.detalles())  # Muestra detalles según el tipo de empleado


# EJEMPLO DE POLIMORFISMO
# ejemplo con figuras geométricas que calculan áreas de manera diferente.

# clase base para figuras
class Figura:
    def area(self):
        pass  # método genérico

# subclase para círculos
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio**2  # fórmula del área del círculo

# subclase para rectángulos
class rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto  # fórmula del área del rectángulo

# uso de las figuras
figuras = [Circulo(5), rectangulo(4, 6)]  # Lista de diferentes figuras
for figura in figuras:
    print(f"Área: {figura.area()}")  # cada figura calcula su área de forma diferente

