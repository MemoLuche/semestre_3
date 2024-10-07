def raiz_cuadrada_binaria(numero):
    precision=0.00001
    if numero < 0:
        return None

    inicio = 0
    fin = numero

    if numero < 1:
        fin = 1

    while (fin - inicio) > precision:
        medio = (inicio + fin) / 2
        if medio * medio == numero:
            return medio
        elif medio * medio < numero:
            inicio = medio
        else:
            fin = medio

    return (inicio + fin) / 2

numero = float(input("Introduce el número para calcular la raíz cuadrada: "))
resultado = raiz_cuadrada_binaria(numero)

if resultado is not None:
    print(f"La raíz cuadrada aproximada de {numero} es {resultado:.5f}")
else:
    print(f"No es posible calcular la raíz cuadrada de un número negativo.")
