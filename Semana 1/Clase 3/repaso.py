#Imprimir un texto simple
print("Buenos días")

#Imprimir varios textos separados por espacios
print("texto1", "texto2")

#concatenar textos
primerTexto = "hola"
segundoTexto = "mundo"
holaMundo = primerTexto + " " + segundoTexto
print(holaMundo)

#formatear textos con variable
miEdad = 10
print(f"yo tengo {miEdad} años")

#nombramiento de variables
#manera 1: PascalCase
VariablePascalCase = "soy una variable con todas las iniciales mayusculas"

#manera 2: camelCase
variableCamelCase = "primera palabra todo minúscula y las siguientes palabras mayúsculas"

#manera 3: snake_case:
variable_snake_case = "poner las palabras separadas por un _"

#operaciones aritméticas
miEdad = 10
edadMiMama = 40

#operacion resta
diferenciaDeEdad = edadMiMama - miEdad
#operacion suma
sumaDeEdades = edadMiMama + miEdad

#operaciones de multiplicacion y división
variable1 = 10
variable2 = 15.5
multiplicacion = variable1 * variable2
division = variable1 / variable2 #cuidado de no dividir por 0 porque sale un error


#jereaquía de las operaciones: potenciación > multiplicacion y división > suma y resta
variable1 = 10
variable2 = 50
variable3 = 20.7
variable4 = -10.1

#primero sumas v1 y v2, despues restar v3 y v4 y dividir esos dos resultados
resultado1 = (variable1 + variable2) / (variable3 - variable4)

#comando de input general de texto
imputDeUsuario = input("por favor ingrese el valor: ")

#comando de input de tipo numerico
inputNumerico = int(input("Por favor ingrese el valor numerico: "))
print(inputNumerico)

