#Ejercicio A
print('Ingresa tu nomnbre:')
nombre = input('Mi nombre es: ')

n = len(nombre) #Encuentra el numero de letras que tiene nombre
print(f'{nombre.upper()} tiene {n} letras') #Imprime en mayusculas el nombre dentro de la frase

#Ejercicio B
print('Ingresa tu fecha de nacimiento con el siguiente formato: dd/mm/aaaa')
nac = input('Mi fecha de nacimiento es: ')
#Separa en distintas variables los valores de la fecha de nacimiento
dia = nac[0:2]
mes = nac[3:5]
anho = nac[6:11]
#Imprime los valores por separado
print(f'Dia: {dia}')
print(f'Mes: {mes}')
print(f'Año: {anho}')

#Ejercicio C
print('Ingresa tu correo electronico')
correo = input('Mi correo es: ')
nprefijo = correo.find('@') #Encuentra la ubicacion del @ dentro del string
prefijo = correo[0:nprefijo] #Sustrae el prefijo del correo
dominio = '@uaq.edu.mx' #Definimos el dominio nuevo del correo
print(f'Tu correo nuevo es: {prefijo + dominio}') #Imprimimos el correo nuevo