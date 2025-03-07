

class Persona(): 
    #asi se crea una clase
    def __init__(self, nombre, edad, telefono, correo, direccion, nacionalidad, profesion): #crear in contructor, siempre se debe poner
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.nacionalidad = nacionalidad
        self.profesion = profesion


persona1 = Persona("Daniel", 50, 5451444, "dlc@c.com", "djdjd","colombiano","ingeniero")
persona2 = Persona("jhon", 42, 45334, "jhon@j.com", "dddkdd", "ingles", "guerrero")
print(persona1.nombre)
print(persona2.nombre)
