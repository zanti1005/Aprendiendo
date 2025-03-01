#paso 1: pedirle al usuario la cantidad de pesonas a ingresar

#paso 2: en un for de 0 a N pedir las edades de esas N personas

#paso 3: guardar las edades de esas personas en una lista

#paso 4: calcular el promedio de esas edades

numberOfPerson = int(input("Por favor ingresa la cantidad de personas: "))

listoOfAges = []

for i in range(0,numberOfPerson):
    listoOfAges.append(int(input("Por favor ingrese la edad de la persona: ")))

averange = sum(listoOfAges) / len(listoOfAges)
print(f"El promedio de las edad es {averange} años")
