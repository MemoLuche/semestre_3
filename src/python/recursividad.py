def suma_digitos(numero):
    # Caso base: si el número es menor que 10, se devuelve el número (último dígito)
    if numero < 10:
        return numero
    else:
        # Caso recursivo: se separa el último dígito y se suma con la llamada recursiva
        return numero % 10 + suma_digitos(numero // 10)

# Ejemplo de uso
numero = 3451
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es {resultado}")
