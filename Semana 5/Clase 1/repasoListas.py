#definir una lista
lista = [1, 5, 2345, 213, -12, 234, 1]
        #0  #1  #2   #3     #4  #5  #6

#imprimir una lista
print(lista)

#acceder a un dato a través del índice
lista[2] = -50
print(lista)

#imprimir un dato específico
print(lista[4])

#agregar un dato al final de una lista
lista.append(17)
print(lista)

#agregar dato en posición específica
lista.insert(0,-500)
print(lista)

#eliminar datos de una lista según su valor
lista.remove(5)
print(lista)

#eliminar datos de una lista por posición
lista.remove(lista[0])
print(lista)

#eliminar el último valor de la lista
lista.pop()
print(lista)

#eliminar un valor por posición
lista.pop(2)
print(lista)

#organizar una lista ascendente
lista.sort()
print(lista)

#revisar si un elemento pertenece a una lista
print(-500 in lista)
print(1 in lista)

#revisar longitud de lista
print(len(lista))

#slicing
print(lista[1:4])
print(lista[:4])
print(lista[1:])