#hacer un juego de adivinanzas
#el numero a adivinar es un aleatorio
#entre 0 y 20
#el código debe generar automáticamente el aleatorio
#ypreguntarle al usuario con un input el numero que quiere adivinar
#el juego debe tener máximo numero de intentos
#si me paso del máximo sin adivinar, pierdo
#si adivino gano

import random

def crearListaNumerosAleatorios(N,rangoInferior, rangoSuperior):
    listaNumerosAleatorios = []
    for numeroAleatorio in range(0, N):
        listaNumerosAleatorios.append(random.randint( ))
    return listaNumerosAleatorios

def buscarNumeroAleatorio(numeroABuscar,listaABuscar):
    encontrar = False
    for index, elemento in enumerate(listaABuscar):
        if elemento == numeroABuscar:
            encontrar = True
            return encontrar
    return encontrar

contJugador = 0
numeroIntentos = 3

listaAleatoria = crearListaNumerosAleatorios(1,0,20)

while contJugador < numeroIntentos:
    
    numeroUsuario = int(input("Por favor ingrese el número 0 a 20 que desea adivinar en la lista: "))
    resultado = buscarNumeroAleatorio(numeroUsuario, listaAleatoria)

    if resultado == False:
        contJugador = contJugador + 1
        print(f"No adivinaste el número te quedan {numeroIntentos-contJugador} intentos.")
    else:
        print("!Ganaste¡, adivinaste el numero.")
        contJugador = numeroIntentos + 1

    #print(listaAleatoria)
    
if contJugador == numeroIntentos:
    print("!Superaste el límite de intentos¡")

