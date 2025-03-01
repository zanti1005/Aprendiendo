listOfGrades=[
    1,
    2.4,
    4.5,
    2.4,
    4.3,
    3.8,
    3.1,
    3,
    2.7,
    4.5,
    5,
    2.1,
    1.8,
    2.4,
    4.3
]

contInsuficiente = 0
contAceptable = 0
contSobreSaliente = 0
sumaInsificiente = 0
sumaAceptable = 0
sumaSobresaliente = 0
for grade in listOfGrades:
    if grade < 3:
        contInsuficiente = contInsuficiente + 1
        sumaInsificiente = sumaInsificiente + grade
    elif grade >= 3 and grade < 4:
        contAceptable = contAceptable + 1
        sumaAceptable = sumaAceptable + grade
    else:
        contSobreSaliente = contSobreSaliente + 1
        sumaSobresaliente = sumaSobresaliente + grade

print("El contador de los insuficinetes es: ", contInsuficiente)
print("El contador de los aceptables es: ", contAceptable)
print("El contador de los sobresalientes es: ", contSobreSaliente)

print("El suma de los insuficinetes es: ", sumaSobresaliente)
print("El suma de los aceptables es: ", sumaAceptable)
print("El suma de los sobresalientes es: ", sumaSobresaliente)

print("El promedio de los insuficinetes es: ", sumaSobresaliente / contInsuficiente)
print("El promedio de los aceptables es: ", sumaAceptable / contAceptable)
print("El promedio de los sobresalientes es: ", sumaSobresaliente / contSobreSaliente)
