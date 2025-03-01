#pedirle al usuario que ingrese su contraseña

#si la contraseña coincide con storedPassword, mostrale un mesaje
    #de inicio de sesión correcto

#Si la contraseña no coincide, mostrale un mensaje de error
    #y pedirle la contraseña nuevamente

maxRetries = 3
storedPassword = "123abc"
userPassword = input("Por favor ingrese su contraseña: ")
cont = 0

while storedPassword != userPassword and cont < maxRetries:
    print("Las contraseñas no coinciden")
    cont = cont + 1
    #forma profesional de contar cont+=1
    userPassword = input("Por favor ingrese la contraseña nuevamente: ")

if cont >= maxRetries:
    print("Te equivocaste mas de 3 veces. Te hemos bloqueado.")
else:
    print("¡Inicio de sesión exitoso!")
