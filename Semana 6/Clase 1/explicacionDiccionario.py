#lista
lista = [1, 2, 50, -500, -10, 20, 35]
print(list[0]) #devuelve 1
#asifnar un valor a un elemento de la lista
lista[0] = -10 #inserta el valor -10 en la primera posición

#tuplas
tupla = (1, -10, -500, 423, 35, 81)
#leer un elemento de la tupla
print(tupla[3])

# clase
class Ejemplo():
    def __init__(self):
        self.atributo1 = 10
        self.atributo2 = -50
        self.atributo3 = -30
        self.atributo4 = 25

ej1 = Ejemplo()
print(ej1.atributo1) #imprime un 10
#modificar un atributo de la clase
ej1.atributo3 = 500
print(ej1.atributo3)


#diccionarios
diccionario1 = {
    "elemento1":10,
    "elemento2":-500,
    "dato1":-20,
    "nombre":"Daniel",
    "apellido":"saldarriaga",
    "ensayo":{
        "d1":10,
        "d2":20,
        "d50":30
    }
}
#acceder a valores dentro del diccionario
print(diccionario1["elemento1"])
print(diccionario1["nombre"])
print(diccionario1["ensayo"]["d1"])

#cambiar un valor del diccionario
diccionario1["dato1"] = -256

print("Diccionario: ",diccionario1)

#acceder a vada key del diccionario
print("Lista de keys: ",diccionario1.keys())

for key in diccionario1.keys():
    print("key: ",key)
    print("value: ",diccionario1[key])


#aceeder a los values del diccionario
print(diccionario1.values())
for value in diccionario1.values():
    print(value)

    #crear una nueva pareja de llave-valor
diccionario1["correo"] = "sbt@b.com"
print(diccionario1)