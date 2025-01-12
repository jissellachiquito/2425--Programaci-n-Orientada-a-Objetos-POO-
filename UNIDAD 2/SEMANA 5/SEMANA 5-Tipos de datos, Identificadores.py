# Este programa convierte una distancia en metros a otras unidades de longitud:
# kilómetros, centímetros y milímetros. También valida que el usuario ingrese
# un número positivo para realizar la conversión.

def convertir_metros(distancia_metros): # Función en snake_case

    """
    Convierte una distancia en metros a kilómetros, centímetros y milímetros.

    Parámetros:
        distancia_metros (float): La distancia en metros que se desea convertir.

    Retorna:
        dict: Un diccionario con las conversiones a kilómetros, centímetros y milímetros.
    """
    conversiones = {    # Variable en snake_case
        "kilometros": distancia_metros / 1000,
        "centimetros": distancia_metros * 100,
        "milimetros": distancia_metros * 1000
    }
    return conversiones


# Bienvenida al usuario
print("Bienvenido al convertidor de unidades.")
print("Con este programa puedes convertir una distancia en metros a otras unidades.\n")

# Pedir al usuario la distancia en metros
distancia_input = input("Por favor, ingresa la distancia en metros: ")

# Validar que sea un número positivo
if distancia_input.replace('.', '', 1).isdigit() and float(distancia_input) > 0:
    distancia_metros = float(distancia_input)
    resultados = convertir_metros(distancia_metros)

    # Mostrar los resultados de las conversiones
    print(f"\nAquí tienes las conversiones para {distancia_metros} metros:")
    print(f"Kilómetros: {resultados['kilometros']:.3f}")
    print(f"Centímetros: {resultados['centimetros']:.1f}")
    print(f"Milímetros: {resultados['milimetros' ]:.1f}")
else:
    print("\nError: Ingresaste un valor inválido. Por favor, ingresa un valor numérico positivo.")
