#pedir al usuario los ingresos
ingresos = float(input("Por favor informe el valor de los ingresos: "))

#pedir al usuario los costos
costos = float(input("Por favor informe el valor de los costos: "))

#calcular la utilidad bruta ingresos - costos
utilidadBruta = ingresos - costos
print(f"El valor de la utilidad bruta fue: ${utilidadBruta}")

#pedirle al usuario los gastos
gastos = float(input("Por favor informe el valor de los gastos: "))

#calcular la utilidad operativa utilidad bruta - gastos
utilidadOperativa = utilidadBruta - gastos

#calcular el impuesto a la renta utilidad operativa * 30%
impuestoRenta = utilidadOperativa*30/100

#calcular utilidad neta utilida brutal - impuesto a la renta
utilidadNeta = utilidadBruta - impuestoRenta

print(f"El valor de la utilidad operativa fue: ${utilidadOperativa}")
print(f"El valor del el impuesto a la renta fue: ${impuestoRenta}")
print(f"El valor de la utilidad neta fue: ${utilidadNeta}")
print("Prueba")