
lista = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39]

##print(lista[0])
i = 0
j = 0
def busquedaBinaria(n, izq, der, contador = 0):
    if izq > der:
        return 'No existe ese objetivo en la lista', contador
    
    medio = (izq + der) // 2

    contador += 1

    if lista[medio] == n:
        return medio, contador
    
    elif lista[medio] < n:
        return busquedaBinaria(n, medio + 1, der, contador)
    
    else:
        return busquedaBinaria(n, izq, medio -1, contador)
    
    ## "Izq" Argumento del valor 0
    ## "Der" Argumento del valor len(lista)
    ## "n" objetivo a encontrar


resultado, pasos = busquedaBinaria(7, 0, len(lista))
print(resultado)
print(f"La cantidad de pasos que dio fueron: {pasos}")