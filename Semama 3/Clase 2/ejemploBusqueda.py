import random

#hacer funcion que reciba un numero N
#y devuelva una lista de numeros aleatorios
#entre 0 y 10
def BuildListOfRandomNumbers(N,inferiorRange, superiorRange):
    listOfRandomNumbers = []
    for randomNumber in range(0, N):
        listOfRandomNumbers.append(random.randint(inferiorRange, superiorRange))
    return listOfRandomNumbers

#buscar si un numerO X esta en la lista de aleatorios.
#en caso de que el numero este devolver la posicion del numero
def searchNumberInRandomList(numberToFind,listToSearch):
    found = False
    for index, element in enumerate(listToSearch):
        if element == numberToFind:
            found = True
            return index
    return found

randomList = BuildListOfRandomNumbers(50, 0, 100)
found = searchNumberInRandomList(19,randomList)
print(randomList)
print(found)