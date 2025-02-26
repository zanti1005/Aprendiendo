#Paso 1: pedir el total de la factura
totalFactura = int(input("Por favor ingrese el valor total de la factura: "))

#Paso2: pedir el porcentaje de la propina que se quiere entregar
porcentajePropina = int(input("Por favor ingrese el valor que quiere dar de propina: "))

#Paso 3: calcular el valor del IVA del 19%
valorIVA = totalFactura * 19 / 100

#Paso 4: calcular subtotal (subtotal de la factura - valor del iva)
subTotal = totalFactura - valorIVA

#Paso 5: calcular el valor de la propina (subtotal * propina / 100)
valorPropina = subTotal * porcentajePropina / 100

#paso 6: mostrar el resultado
print(f"El valor total de la factura fue: {totalFactura}")
print(f"El valor del IVA fue: {valorIVA}")
print(f"El subtotal fue: {subTotal}")
print(f"El valor de la propina fue: {valorPropina}")
print(f"El valor total de la compra mas la propina es ${totalFactura+valorPropina} pesos")

