import numpy as np

#crear lista simple
matriz1 = np.array([1,2,3])
print(matriz1)

#crear matriz de m x n de ceros
matrizCeros = np.zeros((5,3))
print(matrizCeros)

#crear matriz de m x n de unos
matrizUnos = np.ones((4,4))
print(matrizUnos)

#crear matrix de m x n datos alaeatorios entre 0 1
matrizAleatorios = np.random.random((5,5))
print(matrizAleatorios)
matrizAleatoriosEnteros = np.random.randint(1, 100, (4,4))
print(matrizAleatoriosEnteros)

#calcular la suma de la matriz
print(matrizAleatoriosEnteros.sum())
#calcular el minimo
print(matrizAleatoriosEnteros.min())
#calcular el MÁXIMO
print(matrizAleatoriosEnteros.max())

#crear una matriz de numpy a través de una lista de lista
matrizEjemplo = np.array([[10,-234,345,-90,19],
                            [20,36,-90,-32,45],
                            [56,13,17,65,23],
                            [-14,-23,35,23,21],
                            [-500,-32,86,32,50]])
print(matrizEjemplo)

#iterar cada elemento de la matriz
for i in matrizEjemplo:
    for j in i:
        print(j)

#obtener la diagonal de la matriz
diagonal = np.diag(matrizEjemplo)
print(diagonal)

#obtener un elemento
print(matrizEjemplo[2][0])

#obtener el tamaño
print(matrizEjemplo.shape)

