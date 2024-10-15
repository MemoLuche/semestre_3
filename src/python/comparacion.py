import random as rnd

# Búsqueda Binaria Recursiva
def busqueda_binaria_recursiva(arr, objetivo, bajo, alto):
    if bajo > alto:
        return -1  # El elemento no está en la lista
    
    medio = (bajo + alto) // 2  # Encuentra el punto medio

    if arr[medio] == objetivo:
        return medio  # Elemento encontrado
    elif arr[medio] > objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, bajo, medio - 1)  # Buscar en la mitad izquierda
    else:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, alto)  # Buscar en la mitad derecha

# Búsqueda Lineal
def busqueda_lineal(arr, objetivo):
    pasos = 0
    for i in range(len(arr)):
        pasos += 1
        if arr[i] == objetivo:
            return i, pasos  # Elemento encontrado
    return -1, pasos  # Elemento no encontrado

# Comparación de pasos entre Búsqueda Lineal y Búsqueda Binaria Recursiva
def comparar_busquedas(arr, objetivo):
    # Búsqueda binaria con conteo de pasos
    pasos_binaria = 0
    def busqueda_binaria_con_pasos(arr, objetivo, bajo, alto):
        nonlocal pasos_binaria
        if bajo > alto:
            return -1, pasos_binaria
        
        medio = (bajo + alto) // 2
        pasos_binaria += 1
        
        if arr[medio] == objetivo:
            return medio, pasos_binaria
        elif arr[medio] > objetivo:
            return busqueda_binaria_con_pasos(arr, objetivo, bajo, medio - 1)
        else:
            return busqueda_binaria_con_pasos(arr, objetivo, medio + 1, alto)

    # Resultados de las búsquedas
    indice_lineal, pasos_lineal = busqueda_lineal(arr, objetivo)
    indice_binaria, pasos_binaria = busqueda_binaria_con_pasos(arr, objetivo, 0, len(arr) - 1)
    
    return {
        "Búsqueda Lineal": {"Índice": indice_lineal, "Pasos": pasos_lineal},
        "Búsqueda Binaria": {"Índice": indice_binaria, "Pasos": pasos_binaria}
    }

# Ejemplo de uso
arr = list(range(1, 201))  # Lista de 200 elementos, del 1 al 200
objetivo = rnd.choice(arr)
resultados = comparar_busquedas(arr, objetivo)
print(resultados)