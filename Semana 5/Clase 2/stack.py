listaEjemplo = [1, 10, -500, 800, -1234, -543, 123, 45]

print(listaEjemplo)

#primera forma:
#sacar el último dato de la posición 0
#ingresar un dato nuevo de la posicion 
#retirar el dato del elemento 0
datoRetirado = listaEjemplo.pop(0)
print(listaEjemplo)
#agergar un dato en la posición 0
listaEjemplo.insert(0, -500)
print(listaEjemplo)


def retirarDatos(lista):
    elementoRetirado = lista.pop(0)
    return lista


def agregarDato(lista, dato):
    lista.insert(0, dato)
    return lista


print("_________________")

#método 2:
#retirar el último dato de la lista
#y agregar un dato nuevo al final de la lista
listaEjemplo = [-30, 45, 86, 97, -231, -925, 456]
print(listaEjemplo)
#retirar un dato al final de la lista
elementoRetirado = listaEjemplo.pop()
print(elementoRetirado)
print(listaEjemplo)
#agregar un dato al final de la lista
listaEjemplo.append(600)
print(listaEjemplo)


def retirarrDatos(lista):
    lista.pop()
    return lista


def agregarDato(lista, dato):
    lista.append(dato)
    return lista
print(listaEjemplo)