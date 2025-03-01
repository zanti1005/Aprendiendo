
listOfNumebers = [-10, 50, 800, 9, 6, 23.5]
print(len(listOfNumebers))

cont = 0
for element in listOfNumebers:
    cont = cont +1

print("El total de elementos en la lsita es: ", cont)

suma = 0
for element in listOfNumebers:
    suma = suma + element
print("La suma de los elementos en la lista es: ", suma)
print("El promedio de los datos es: ", suma / cont)