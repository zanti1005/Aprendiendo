# ejercicio 4: hacer un sistema de calificaciones
    #pedir la calificacion de un examen del usuario (0-5)
    #0 - 3: imprimir "insuficiente"
    #3 - 4: imprimir "aceptable"
    #4 - 4.5: imprimir "sobre saliente"
    #4.5 - 5: imprimir "calificacion > 4 and calificacion <= 4.5:"
    #en cualquiero otr rango, imprimir "calificacion inválida"

calificacion = float(input("Por favor ingrese el valor de la calificación de 0 a 5: "))

if calificacion >= 0 and calificacion <= 5:
    #calculo de la calificación
    if calificacion >= 0 and calificacion <= 3:
        print("insuficiente")
    elif calificacion > 3 and calificacion <= 4:
        print("aceptable")
    elif calificacion > 4 and calificacion <= 4.5:
        print("sobre saliente")
    else:
        print("excelente")
else:
    print("calificacion inválida")