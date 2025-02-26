#Paso 1: pedirle al usuario el total de la factura
totalFactura = int(input("Por favor ingrese el valor total de la factura: "))

#Paso 2: pedirle al usuario eñ valor que quiere dar de propina
valorPropina = int(input("Por favor ingrese el valor que quiere dar de propina: "))

#Paso 3: hacer el cálculo de la propina
propina = totalFactura * valorPropina / 100

#Paso 4: mostrale al usuario el valor de la propina
print(f"El valor de la propina es: ${propina} pesos")