#imprimir la suma, la resta y la multiplicación de dos números enteros

def addTwoNumbers(n1, n2):
    suma = n1 + n2
    return suma

#definir la funciones de resta
def subtractTwoNumbers(n1, n2):
    return n1 - n2

#definir la funcion de multiplicar
def multiplyTwoNumbers(n1, n2):
    return n1 *  n2

#funcion general para el cálculo
def calculateResult(n1,n2,operation): #operation: s, r , m
    result = 0
    if operation == "s":
        result = addTwoNumbers(n1,n2)
    elif operation == "r":
        result = subtractTwoNumbers(n1,n2)
    elif operation == "m":
        result = multiplyTwoNumbers (n1,n2)
    else:
        result = "error"
    return result

number1 = int(input("por favor ingrese el primer número: "))
number2 = int(input("por favor ingrese el segundo número: "))

suma = calculateResult(number1, number2,"s")
resta = calculateResult(number1, number2,"s")
multiplicacion = calculateResult(number1, number2,"s")

print("La suma es : ", suma)
print("La resta es : ", resta)
print("La multiplicación es : ", multiplicacion)