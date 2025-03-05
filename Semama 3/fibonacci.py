#write a python program to get the fibonacci series between 0 to 50.
#the fibonacci sequence is the series of numeber: 0, 1, 1, 2, 3, 5, 8, 13, 21

listFibonacci = [0,1]

cont = 1
while len(listFibonacci)<50:
    listFibonacci.append(listFibonacci[cont] + listFibonacci[cont-1])
    cont += 1

print(listFibonacci)
