from persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, edad, telefono, correo, documento, direccionEnvio, correoFacturacion):
        super().__init__(nombre, edad, telefono, correo, documento)
        self.acumuladoCompra = 0
        self.direccionEnvio = direccionEnvio
        self.correoFacturacion = correoFacturacion

    
    def acumular(self, monto):
        self.acumuladoCompra = self.acumuladoCompra + monto
        
    def revisarDescuento(self, randoDescuento):
        if self.acumuladoCompra >= randoDescuento:
            return True
        else:
            return False