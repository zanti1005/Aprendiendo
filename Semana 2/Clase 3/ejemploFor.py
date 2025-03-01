
names = ["Daniel","Jose","Miguel","Ana","Carolina"]


for element in names:
    print(element)


listOfNumbers = [10, 50, -5, 20, -30.4]

for nubmer in listOfNumbers:
    if nubmer > 15:
        print(nubmer)


list3 = ["Hola","hoy",345,89]
print(list3[0])

for index,element in enumerate(list3):
    print(index, element)


matrix = [[1,2,3],[4,5,6],[7,8,9]]

for row in matrix:
    print(row)
    for element in row:
        print(element)