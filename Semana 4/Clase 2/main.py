from tienda import Tienda
from producto import Producto

#3:
nombreTienda = input("Ingrese el nombre de la tienda a crear: ")
paginaWeb = input("Ingrese la página web de la tienda: ")
direccion = input("Ingrese la dirección  de la tienda: ")
tienda = Tienda(nombreTienda,paginaWeb,direccion)


#7:
while True:
    instrucciones = """
    Ingrese NP para crear nuevo producto,
    I para imprimir los productos e inventarios
    V para ejecutar la venta
"""
    operacion = input(instrucciones)
    if operacion == "NP":
        #6:
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        productoCreado = Producto(nombre,precio)
        tienda.agregarProducto(productoCreado)
    elif operacion == "I":
        tienda.imprimirProductosEinventarios() 
    elif operacion == "V":
        #9
        nombreProducto = input("Ingrese el nombre del producto que quiere comprar: ")
        productoEncontrado = tienda.buscarProductoPorNombre(nombreProducto)
        if not productoEncontrado:
            print("El producto no fue encontrado")
        else:
            cantidadAComprar = int(input("Ingese cantidad a comprar: "))
            if productoEncontrado.inventario >= cantidadAComprar:
                total = productoEncontrado.precio * cantidadAComprar
                print(f"Venta exitosa, el total de la venta es: ${total} pesos")
                #productoEncontrado.inventario 
                productoEncontrado.inventario -= cantidadAComprar
            else:
                print("No hay inventario suficiente de la referencia que desea comprar")