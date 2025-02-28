# ejercicio 3: preguntar el total de una compra.
    # si el valor es mayor a 100.000, dar un descuento del 10%

totalCompra = float(input("Por favor ingrese el de la compra: "))

descuento = 0
if totalCompra > 100000:
     descuento = totalCompra * 10 / 100
     print(f"El valor del descuento es ${descuento}")
else:
     descuento = 0

finalCompra = totalCompra - descuento
print(f"El valor total de la compra es ${finalCompra}")