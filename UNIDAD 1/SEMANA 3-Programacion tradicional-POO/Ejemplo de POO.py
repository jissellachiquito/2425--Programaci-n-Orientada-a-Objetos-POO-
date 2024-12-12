# Programación Orientada a Objetos

class climadiario:
    """Clase que representa la información diaria del clima."""

    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """Solicita las temperaturas diarias al usuario y las almacena en una lista."""
        for dia in range(7):
            temperatura = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
            self.temperaturas.append(temperatura)

    def calcular_promedio(self):
        """Calcula y devuelve el promedio de las temperaturas almacenadas."""
        return sum(self.temperaturas) / len(self.temperaturas)

# Uso de la clase
print("\n=== Programa de calculo de promedio de temperaturas ===")
clima = climadiario()
clima.ingresar_temperaturas()
promedio = clima.calcular_promedio()
print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados.")