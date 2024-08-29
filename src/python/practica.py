
def practica1():
    # Lista de asignaturas
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

    # Recorre la lista y muestra el mensaje para cada asignatura
    for asignatura in asignaturas:
        print(f"Yo estudio {asignatura}")

def practica2():
    # Lista para almacenar los pesos de los estudiantes
    pesos = []

    # Pedir al usuario el peso de 7 estudiantes
    for i in range(7):
        peso = float(input(f"Ingrese el peso del estudiante {i+1}: "))
        pesos.append(peso)

    # Ordenar la lista de pesos de menor a mayor
    pesos.sort()

    # Mostrar la lista ordenada
    print("Los pesos ordenados de menor a mayor son:")
    for peso in pesos:
        print(peso)

def practica3():
    # Lista de asignaturas
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

    # Lista para almacenar las asignaturas que se deben repetir
    asignaturas_para_repetir = []

    # Pedir al usuario la nota de cada asignatura
    for asignatura in asignaturas:
        nota = float(input(f"Ingrese la nota que obtuvo en {asignatura}: "))
        if nota <= 5:
            asignaturas_para_repetir.append(asignatura)

    # Mostrar las asignaturas que el usuario tiene que repetir
    if asignaturas_para_repetir:
        print("Debe repetir las siguientes asignaturas:")
        for asignatura in asignaturas_para_repetir:
            print(asignatura)
    else:
        print("¡Felicidades! No tienes que repetir ninguna asignatura.")

def practica4 ():
    # Lista del abecedario
    abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # Eliminar las letras en posiciones que son múltiplos de 3
    abecedario_filtrado = [letra for i, letra in enumerate(abecedario) if (i + 1) % 3 != 0]

    # Mostrar la lista resultante
    print("El abecedario después de eliminar las posiciones múltiplos de 3 es:")
    print(abecedario_filtrado)

def practica5 ():
    # Pedir al usuario una palabra
    palabra = input("Ingrese una palabra: ")

    # Convertir la palabra a minúsculas y eliminar espacios para la verificación
    palabra_limpia = palabra.replace(" ", "").lower()

    # Verificar si la palabra es un palíndromo
    if palabra_limpia == palabra_limpia[::-1]:
        print(f"La palabra '{palabra}' es un palíndromo.")
    else:
        print(f"La palabra '{palabra}' no es un palíndromo.")

def practica6 ():
    # Pedir al usuario una palabra
    palabra = input("Ingrese una palabra: ").lower()

    # Diccionario para contar las vocales
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Contar las vocales en la palabra
    for letra in palabra:
        if letra in vocales:
            vocales[letra] += 1

    # Mostrar el número de veces que aparece cada vocal
    for vocal, cantidad in vocales.items():
        print(f"La vocal '{vocal}' aparece {cantidad} veces.")

print('Que programa quiere ejecutar 1-6')
opcion = input('Opcion deseada: ')

