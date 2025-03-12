#escriba una clase de pyhton llamada rectángulo construido por una longitud y un ancho con un método que clacule el área

class rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        self.area = self.base * self.altura
        print("El valor del área del retándulo es: ",self.area)

base = float(input("Digite el valor de la base del rectángulo: "))
altura = float(input("Digite el valor de la altura del rectángulo: "))

operacion = rectangulo(base,altura)
operacion.calcularArea()