def raiz_cuadrada_exhaustiva(objetivo):
    epsilon = 0.0001  # Precisión
    paso = 0.0001  # Tamaño del paso
    respuesta = 0.0
    
    while respuesta**2 < objetivo and respuesta <= objetivo:
        respuesta += paso
        
    if abs(respuesta**2 - objetivo) >= epsilon:
        return None  # No se encontró la raíz exacta con la precisión dada
    else:
        return respuesta

def raiz_cuadrada_aproximacion(objetivo):
    epsilon = 0.0001  # Precisión deseada
    paso = epsilon**2  # Definimos un tamaño de paso que es pequeño
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        return None  # No se encontró una raíz exacta
    else:
        return respuesta

def raiz_cuadrada_busqueda_binaria(objetivo):
    epsilon = 0.0001  # Precisión
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2

    return respuesta

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Método exhaustivo")
    print("2. Método de aproximación")
    print("3. Método de búsqueda binaria")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "4":
            print("Saliendo del programa...")
            break
        elif opcion in ("1", "2", "3"):
            numero = float(input("Ingresa el número para encontrar la raíz cuadrada: "))

            if opcion == "1":
                resultado = raiz_cuadrada_exhaustiva(numero)
                metodo = "exhaustivo"
            elif opcion == "2":
                resultado = raiz_cuadrada_aproximacion(numero)
                metodo = "de aproximación"
            elif opcion == "3":
                resultado = raiz_cuadrada_busqueda_binaria(numero)
                metodo = "de búsqueda binaria"

            if resultado is not None:
                print(f"La raíz cuadrada de {numero} usando el método {metodo} es aproximadamente {resultado}")
            else:
                print(f"No se pudo encontrar una raíz cuadrada exacta para {numero} con el método {metodo}.")
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el programa
main()
