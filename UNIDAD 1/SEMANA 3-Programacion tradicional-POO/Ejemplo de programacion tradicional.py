# Programación Tradicional

def ingresar_temperaturas():
    """Solicita las temperaturas diarias al usuario y las devuelve en una lista."""
    temperaturas = []
    for dia in range(7):
        temperatura = float(input(f"Ingrese la temperatura del día {dia + 1}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio(temperaturas):
    """Calcula y devuelve el promedio de una lista de temperaturas."""
    return sum(temperaturas) / len(temperaturas)

def main():
    """Función principal que organiza la lógica del programa."""
    print("\n=== Programa de cálculo de promedio de temperaturas ===")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados.")

# Llamada a la función principal
main()
