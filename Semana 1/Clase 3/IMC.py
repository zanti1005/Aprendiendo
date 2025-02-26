#paso1: pedirle al usuarioe su peso
peso = int(input("Por favor ingrese su peso en kg: "))

#paso 2: pedirle al usuario su estatura 
estatura = float(input("Por favor ingrese su estatura en m: "))

#paso3: calcular el IMC
imc= peso / (estatura ** 2)

#PASO 4: mostra el IMC dependiendo del caso

if imc >= 25:
    print(f"Ojo, tienes sobrepeso. Tu IMC es de {imc} kg/m2")
else:
    print(f"No tienes sobrepeso. Tu IMC es de {imc} kg/m2")
