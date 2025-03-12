
contP1 = 0
contP2 = 0

while (contP1 < 2) and (contP2 < 2):

    player1 = input("Ingrese R, O o S: ") #R: rock, P: paper, S: scissors
    player2 = input("Ingrese R, O o S: ") #R: rock, P: paper, S: scissors

    if player1 == player2:
        print("Empate")

    if player1 == "R" and player2 == "S":
        print("El jugador 1 gana")
        contP1 = contP1 + 1
    elif player2 == "R" and player1 == "S":
        print("El jugador 2 gana")
        contP2 = contP2 + 1

    if player1 == "P" and player2 == "R":
        print("El jugador 1 gana")
        contP1 = contP1 + 1
    elif player2 == "P" and player1 == "R":
        print("El jugador 2 gana")
        contP2 = contP2 + 1

    if player1 == "S" and player2 == "P":
        print("El jugador 1 gana")
        contP1 = contP1 + 1
    elif player2 == "S" and player1 == "P":
        print("El jugador 2 gana")
        contP2 = contP2 + 1
    
    print("El jugador 1 ha ganado: ", contP1)
    print("El jugador 2 ha ganado: ", contP2)

if contP1 == 2:
    print("El jugador 1 ganó 2 veces")

if contP2 == 2:
    print("El jugador 2 ganó 2 veces")