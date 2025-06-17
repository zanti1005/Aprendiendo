from persona import Persona

class Vendedor(Persona):
    def __init__(self, nombre, edad, telefono, correo, documento, objetivoVentas, IDempresarial):
        super().__init__(nombre, edad, telefono, correo, documento)
        self.objetivoVentas = objetivoVentas
        self.IDempresarial = IDempresarial
        self.acumuladoVentas = 0

    def acumular(self,monto):
        self.acumuladoVentas = self.acumuladoVentas + monto

    def revisarObjetivo(self):
        if self.acumuladoVentas > self.objetivoVentas:
            print("El objetivo se ha cumplido")
        else:
            print(
                f"Aún no se ha cumnplido el objetivo. Faltan {self.objetivoVentas-self.acumuladoVentas}")


        print(f"Objetivo: {self.objetivoVentas}")
        print(f"Acumulado: {self.acumuladoVentas}")