#pedirle al usuario dos valores númricos. Imprimir el mayor de ellos.

primero = float(input("Por favor ingrese el primer valor numérico: "))

segundo = float(input("Por favor ingrese el segundo valor numérico: "))

if primero > segundo:
    print(f"El número mayor es el primero {primero}")
elif primero < segundo:
    print(f"El número mayor es el segundo {segundo}")
else:
    print("Los numeros son iguales. No hay ningun mayor")