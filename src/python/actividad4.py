def busqueda_exhaustiva(numero, precision=0.0001):
    respuesta = 0.0
    incremento = precision
    
    while abs(respuesta ** 2 - numero) >= precision and respuesta <= numero:
        respuesta += incremento
    
    if abs(respuesta ** 2 - numero) >= precision:
        return None  # No se encontró una raíz precisa
    return respuesta

def busqueda_binaria(numero, precision=0.0001):
    bajo = 0.0
    alto = max(1.0, numero)
    respuesta = (alto + bajo) / 2
    while abs(respuesta ** 2 - numero) >= precision:
        if respuesta ** 2 < numero:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2
    return respuesta

def metodo_aproximacion(numero, precision=0.0001):
    respuesta = numero
    while abs(respuesta ** 2 - numero) >= precision:
        respuesta = (respuesta + numero / respuesta) / 2
    return respuesta

def elegir_algoritmo():
    print("Elige el algoritmo para calcular la raíz cuadrada:")
    print("1. Búsqueda Exhaustiva")
    print("2. Búsqueda Binaria")
    print("3. Método de Aproximación (Newton-Raphson)")
    opcion = int(input("Ingresa el número de tu elección: "))
    
    numero = float(input("Ingresa el número del que deseas calcular la raíz cuadrada: "))
    
    # Fijamos la precisión para todos los métodos en 0.0001
    precision = 0.0001
    
    if opcion == 1:
        resultado = busqueda_exhaustiva(numero, precision)
    elif opcion == 2:
        resultado = busqueda_binaria(numero, precision)
    elif opcion == 3:
        resultado = metodo_aproximacion(numero, precision)
    else:
        print("Opción no válida.")
        return

    if resultado is not None:
        print(f"La raíz cuadrada aproximada de {numero} es {resultado}")
    else:
        print("No se encontró una raíz cuadrada con la precisión indicada.")

# Ejecutar el programa
elegir_algoritmo()
