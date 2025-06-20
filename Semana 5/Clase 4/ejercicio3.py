import numpy as np

matrizEjemplo = np.array([[10,-234,345,-90,19],
                            [20,36,-90,-32,45],
                            [56,13,17,65,23],
                            [-14,-23,35,23,21],
                            [-500,-32,86,32,50]])

tamano = matrizEjemplo.shape
print(tamano)

sumatoriaDiagonalPpal = 0
productoDiagonalInversa = 1

for index, data in np.ndenumerate(matrizEjemplo):
    #identificar el valor i y j de cada dato de la matriz
    i = index[0]
    j = index[1]

    #identificar si un dato esta en la diagonal principal
    if i == j:
        print("diagonal ppal: ", data)
        if data > 20:
            #obtener la suma de los datos mayores a 20
            sumatoriaDiagonalPpal = sumatoriaDiagonalPpal + data

    #identificar si un dato esta en la diagonal inversa
    if (tamano[0] - i -1) == j:
        print("diagonal inversa: ", data)
        if data < 0:
            #obtener productoria de los datos negativos
            productoDiagonalInversa = productoDiagonalInversa * data

    print("Sumatoria", sumatoriaDiagonalPpal)
    print("producto", productoDiagonalInversa)
    #sumar ambos resultados
    print("resultado final", sumatoriaDiagonalPpal,productoDiagonalInversa)
