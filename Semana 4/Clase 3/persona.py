class Persona(): 
    #asi se crea una clase
    def __init__(self, nombre, edad, telefono, correo, documento): #crear in contructor, siempre se debe poner
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.correo = correo
        self.documento = documento

class Vendedor(Persona):
    def __init__(self, nombre, edad, telefono, correo, documento, objetivoVentas, IDempresarial):
        super().__init__(nombre, edad, telefono, correo, documento)
        self.objetivoVentas = objetivoVentas
        self.IDempresarial = IDempresarial
        self.acumulado = 0

class Cliente(Persona):
    def __init__(self, nombre, edad, telefono, correo, documento, direccionEnvio, correoFacturacion):
        super().__init__(nombre, edad, telefono, correo, documento)
        self.acumuladoFacturacion = 0
        self.direccionEnvio = direccionEnvio
        self.correoFacturacion = correoFacturacion