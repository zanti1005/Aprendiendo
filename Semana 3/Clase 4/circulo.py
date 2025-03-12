#crear una clase en python llamada círculo contruido por un radio y métodos 
#que contrullan el área y perímetro del círculo.

import math
pi = math.pi

class circulo:
    def __init__ (self, radio):
        self.radio = radio

    def calcularArea(self):
        self.area = pi * (self.radio**2)
        print("El valor del área del círculo es: ",self.area)

    def calcularPerimetro(self):
        self.perimetro = (2*pi) * self.radio
        print("El valor del perímetro del círculo es: ",self.perimetro)

radio = float(input("Digite el valor del radio del círculo: "))
operacion = circulo(radio)
operacion.calcularArea()
operacion.calcularPerimetro()
