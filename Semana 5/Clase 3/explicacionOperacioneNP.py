import numpy as np
matrizEjemplo = np.array([[10,-234,345,-90,19],
                            [20,36,-90,-32,45],
                            [56,13,17,65,23],
                            [-14,-23,35,23,21],
                            [-500,-32,86,32,50]])
print("Matriz:")
print(matrizEjemplo)
#sacar una suma de los elementos para cada fila
print("Suma de elementos de cada fila:")
print(matrizEjemplo.sum(axis=1))

#sacar una suma de elementos para cada columna
print("Suma de elementos de vada columna:")
print(matrizEjemplo.sum(axis=0))

#sacar el máximo de cada fila
print("Máximo de cada fila:")
print(matrizEjemplo.max(axis=1))
print("Máximo de cada columna:")
#sacar elmáximo de cada columna
print(matrizEjemplo.max(axis=0))

#sacar el minimo de cada fila
print("Mínimo de cada fila:")
print(matrizEjemplo.min(axis=1))
print("Mímino de cada columna:")
#sacar el mínimo de cada columna
print(matrizEjemplo.min(axis=0))


#calcular la matriz triangular superior:
triangularSuperior = np.triu(matrizEjemplo)
print("Triángular superior")
print(triangularSuperior)

#calcular la matriz triangular inferior:
triangularInferior = np.tril(matrizEjemplo)
print("Triángular inferior")
print(triangularInferior)

#calcular la transpuesta de una matriz
print("Matriz:")
print(matrizEjemplo)
transpuesta = np.transpose(matrizEjemplo)
print("transpuesta: ")
print(transpuesta)
