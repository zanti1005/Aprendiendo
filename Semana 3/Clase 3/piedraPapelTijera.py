#hacer un juego de piedra papel o tijera contra
#el computador. el computador escoge aleatoriamente piedra papel o tijera
# y debe pedir al usuario su input
#el juego debe terminar cuando alguno de los dos gane 2 de 3 partidas

import random

# para q el pc escoga p, p o t
def machinSelection():
    randomNomber = random.randint(1,3)
    if randomNomber == 1: #piedra
        return "R"
    elif randomNomber == 2: #papel
        return "P"
    elif randomNomber == 3: #tijera
        return "S"

def evaluateRockPaperScissorsCondition(machine, user):
    if machine == user:
        return "Empate"

    if machine == "R" and user == "S":
        return "machine"
    elif user == "R" and machine == "S":
        return "user"

    if machine == "P" and user == "R":
        return "machine"
    elif user == "P" and machine == "R":
        return "user"

    if machine == "S" and user == "P":
        return "machine"
    elif user == "S" and machine == "P":
        return "user"


def playRockPaperScissor():
    contMachine = 0
    contUser = 0
    while contMachine < 2 and contUser < 2:
        machine = machinSelection()
        print(machine)
        user = input("Por favor ingreso su selección (R,P,S): ")
        result = evaluateRockPaperScissorsCondition(machine,user)
        if result == "machine":
            contMachine = contMachine + 1
            print("La maquina gana")
        elif result == "user":
            contUser = contUser + 1
            print("El usuario gana")
        else:
            print("Empate")

        print("user",contUser)
        print("machine",contMachine)

    if contMachine == 2:
        return "machine"
    elif contUser == 2:
        return "user"

winner = playRockPaperScissor()
print("El ganador definitivo es: ", winner)