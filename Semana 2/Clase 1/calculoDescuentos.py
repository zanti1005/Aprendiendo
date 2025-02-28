
# precio de base de los huevos = 1800
# precio de base de los arepas = 5000

# si alguien compra mas de 10 canastas, el precio es 1000

# si alguien compra mas de 10 canastas de huevos y ademas compra 10 paquetes de arepas
# el precio de los huevos es 800 y las arepas 2000

# paso 1: preguntar cuantos huevos quiere comprar la persona
cantidadDeHuevos = int(input("Digite la cantidad de canastas que quiere comprar: "))

# paso 2: preguntar si la persona quiere comprar arepas
quiereArepas = input("¿Usted desea llevar arepas? ").lower()#comando para poner todo en minusculas
cantidadArepas = 0

# paso 3: si la persona quiere comprar arepas, preguntarle cuantas
if quiereArepas == "si" or quiereArepas == "sí":
    cantidadArepas = int(input("Digite la cantidad de paquetes de arepas que quiere comprar: "))

# paso 4: calcular el total de la compra
precioHuevos = 1800
precioArepas = 5000

if cantidadDeHuevos > 10:
    precioHuevos = 1000
    precioArepas = 5000

if cantidadArepas > 10 and cantidadDeHuevos > 10:
    precioHuevos = 800
    precioArepas = 2000

subTotal = precioHuevos*cantidadDeHuevos + precioArepas*cantidadArepas 
print(f"El total de su compra es ${subTotal} pesos")

#if subTotal > 50000 and (cantidadDeHuevos == 0 or cantidadArepas == 0):
#    descuento = subTotal * 10 / 100
#    totalFinal = subTotal - descuento
 #   print(f"El descuento de la compra es de ${descuento} ")
  #  print(f"El total final de la compra es de ${totalFinal}")
#elif subTotal > 50000 and (cantidadDeHuevos > 0 and cantidadArepas > 0):
 #   descuento = subTotal * 15 / 100
  #  totalFinal = subTotal - descuento
   # print(f"El descuento de la compra es de ${descuento} ")
    #print(f"El total final de la compra es de ${totalFinal}")

descuento = 0
if subTotal > 50000:
    if cantidadDeHuevos == 0 or cantidadArepas == 0:
        descuento = subTotal * 10 / 100
    else:
        descuento = subTotal * 15 / 100

total = subTotal  - descuento

# Condiciones adicionales que se deben cumplir
# 1. si total de la compra es mayor a 50000 dar un descuento adicional del 10%

# 2. si el total de la compra es mayor a 50000 y ademas estan comprando huevos y arepa 
# el descuento no es 10% si no que es 15%

#mostrarle al usuario el total de la compra y el total del descuento