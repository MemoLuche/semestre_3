magos = {'Alicia', 'David', 'Carolina'}

for mago in magos:
    print(mago)

print('\n')
print(magos)

pares = list(range(2,11,2))
print(pares)

cuadrados = list()
for num in range (1,11):
    cuadrados.append(num**2)
print(cuadrados)

cuadrados2 = [valor ** 2 for valor in range in (1,11)]
print(cuadrados2)