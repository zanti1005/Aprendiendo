import random

#hacer una clae que se llame cuenta bancaria
#atribitos:
#numero de la cuenta -> es aleatorio entre 1.000 y 10.000
#Saldo
#metodos:
#retirar
#depositar

#ejercicio: agregar condicion para que saque error si el saldo es negativo
#ejercicio: cobrar una comsion de 4 pesos por cada 1000 cuando el monto de la consignacion sea mayor a 10.000

#ejercicio opcional: crear una lista de cuenbta y agregar la posibilidad de crear una cuenta nueva o eliminar una cuenta
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
        self.saldo = self.saldo + monto

    def consultarSaldo(self):
        print("Cuenta: ",self.numeroCuenta)
        print("Saldo :",self.saldo)
        print("_______________")


saldoInicial = float(input("Bienvenido al banco XYZ. Para crear su cuenta bancaria, ingrese el saldo inicial de la cuenta: "))
cuenta = CuentaBancaria(saldoInicial)
while True:
    operacion = input("Ingrese S para consultar el saldo, R para retirar y C para consignar: ")
    if operacion == "S":
        cuenta.consultarSaldo()
    elif operacion == "R":
        monto = float(input("Ingrese el monto que quiere retirar: "))
        cuenta.retirar(monto)
    elif operacion == "C":
        monto = float(input("Ingrese el monto que quiere consignar: "))
        cuenta.consignar(monto)
        print("Consignación exitosa")
    else:
        print("Operación incorrecta")
