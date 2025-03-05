numeroIngresadoPorElUsuario = 0
numeroAEncontrar = 7

while numeroIngresadoPorElUsuario != numeroAEncontrar:
    numeroIngresadoPorElUsuario = int(input("Adivina cuál número esta registrado como variable: "))
    if numeroIngresadoPorElUsuario > numeroAEncontrar:
        print("EL numero que estas buscando es menor al que encontraste")
    elif   numeroIngresadoPorElUsuario < numeroAEncontrar:
        print("EL numero que estas buscando es mayor al que encontraste")

print("¡Correcto! El número que ingesaste es el correcto")   