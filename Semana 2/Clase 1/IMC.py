#paso1: pedirle al usuarioe su peso
peso = int(input("Por favor ingrese su peso en kg: "))

#paso 2: pedirle al usuario su estatura 
estatura = float(input("Por favor ingrese su estatura en m: "))

#paso3: calcular el IMC
imc= peso / (estatura ** 2)

#PASO 4: mostra el IMC dependiendo del caso


if imc < 18.5:
    print("Usted tiene una condición de peso inferior al normal")
elif imc >= 18.5 and imc < 24.9:
    print("Usted tiene una condición de peso normal")
elif imc >= 25 and imc < 29.9:
    print("Usted tiene una condición de peso superior al normal")
else:
    print("Usted tiene sobre peso")

print(f"Su indice de masa corporal es de {imc} kg/m2")
