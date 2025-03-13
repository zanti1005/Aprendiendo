import random

#ejercicio opcional: crear una lista de cuenbta y agregar la posibilidad 
# de crear una cuenta nueva o eliminar una cuenta
#cuando se vaya a retirar o a consignar se debe ingresra el numero de la cuenta

#Crear una clase persona y a la clase cuenta agregrale una persona pidiéndole una cédula
# Hay que contruir una lista de persona. Si la persona no existe, se debe crear

class CuentaBancaria:
    def __init__(self, saldoInicial):
        self.numeroCuenta = random.randint(1000,10000)
        self.saldo = saldoInicial
    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo = self.saldo -  monto
            print("Retiro Exitoso")
    def consignar(self, monto):
        if monto > 10000:
            comision = monto * 4 / 1000
            monto = monto - comision
            print("La comisión por la consignación es de: ", comision)
            self.saldo = self.saldo + monto
        else:
            self.saldo = self.saldo + monto
    def consultarSaldo(self):
        print("Cuenta: ",self.numeroCuenta)
        print("Saldo :",self.saldo)
        print("_______________")

def buscarCuentas(mensajeOperacion, listaDeCuentas):
    #pedir el numero de la cuenta al usuario
    numCuenta = int(input(mensajeOperacion))
    #buscar la cuenta del usuario.Cuando se encuentre imprimir el saldo
    for cuentaIteracion in listaDeCuentas:
        if cuentaIteracion.numeroCuenta == numCuenta:
            return [True,cuentaIteracion]
    return [False]

listaDeCuentas = []

while True:
    operacion = input("Ingrese N para crear una nueva cuenta, S para consultar el saldo, R para retirar y C para consignar: ")
    if operacion == "N":
        saldoInicial = float(input("Bienvenido al banco XYZ. Para crear su cuenta bancaria, ingrese el saldo inicial de la cuenta: "))
        nuevaCuenta =CuentaBancaria(saldoInicial)
        listaDeCuentas.append(nuevaCuenta)
        print("Cuenta creada con éxito. El número de la cuenta es ", nuevaCuenta.numeroCuenta)
    elif operacion == "S":
        resultadoBusqueda = buscarCuentas("Por favor ingrese la cuenta que quiere consultar ", listaDeCuentas)
        if resultadoBusqueda[0]:
            cuentaEncontrada = resultadoBusqueda[1] 
            cuentaEncontrada.consultarSaldo()
        else:
            print("Cuenta no encontrada")
    elif operacion == "R":
        resultadoBusqueda = buscarCuentas("Por favor ingrese la cuenta que quiere retirar ", listaDeCuentas)
        if resultadoBusqueda[0]:
            cuentaEncontrada = resultadoBusqueda[1]
            monto = float(input("Ingrese el monto que quiere retirar: "))
            cuentaEncontrada.retirar(monto)
        else:
            print("Cuenta no encontrada")
    elif operacion == "C":
        resultadoBusqueda = buscarCuentas("Por favor ingrese la cuenta a la que quiere consignar ", listaDeCuentas)
        if resultadoBusqueda[0]:
            monto = float(input("Ingrese el monto que quiere consignar: "))
            cuentaEncontrada = resultadoBusqueda[1]
            cuentaEncontrada.consignar(monto)
            print("Consignación exitosa")
        else:
            print("Cuenta no encontrada")
    else:
        print("Operación incorrecta")
