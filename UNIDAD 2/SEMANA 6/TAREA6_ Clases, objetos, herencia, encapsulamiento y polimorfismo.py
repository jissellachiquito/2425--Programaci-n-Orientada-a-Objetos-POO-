# Ejemplos que demuestra herencia, encapsulación y polimorfismo.
# Programa de un sistema simple donde se representan personas, estudiantes y profesores.
# - Herencia: La clase base 'Persona' es extendida por las clases derivadas 'Estudiante' y 'Profesor'.
# - Encapsulación: Se protegen atributos como la edad mediante métodos getter y setter.
# - Polimorfismo: Métodos sobrescritos permiten que las clases derivadas personalicen su comportamiento.

# Clase base: Persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self._edad = edad    # Atributo protegido

    # Método para mostrar información de la persona
    def mostrar_información(self):
        return f"Nombre: {self.nombre}, Edad: {self._edad}"

    # Método para obtener la edad (encapsulación)
    def get_edad(self):
        return self._edad

    # Método para modificar la edad (encapsulación)
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self._edad = nueva_edad
        else:
            print("La edad debe ser un valor positivo.")

# Clase derivada: Estudiante (hereda de Persona)
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.grado = grado  # Atributo adicional para Estudiante

    # Método sobrescrito para mostrar información
    def mostrar_información(self):
        return f"Nombre: {self.nombre}, Edad: {self._edad}, Grado: {self.grado}"

# Clase derivada: Profesor (hereda de Persona)
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    # Método sobrescrito para mostrar información (polimorfismo)
    def mostrar_información(self):
        return f"Nombre: {self.nombre}, Edad: {self._edad}, Materia: {self.materia}"

# Uso del programa, se demuestra el uso de estos conceptos creando instancias de las clases y mostrando su información.
def main():
    # Instancia de la clase Persona
    persona = Persona("Ana", 35)
    print(persona.mostrar_información())

    # Modificamos la edad usando encapsulación
    persona.set_edad(36)
    print(f"Edad modificada: {persona.get_edad()}")

    # Instancia de la clase Estudiante
    estudiante = Estudiante("Carlos", 20, "Ingeniería")
    print(estudiante.mostrar_información())

    # Instancia de la clase Profesor
    profesor = Profesor("María", 45, "Matemáticas")
    print(profesor.mostrar_información())

    # Uso de polimorfismo
    personas = [persona, estudiante, profesor]
    print("\n--- Información usando polimorfismo ---")
    for p in personas:
        print(p.mostrar_información())

if __name__ == "__main__":
    main()
