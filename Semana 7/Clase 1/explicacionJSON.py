import json

diccionario = {
    "lenguaje":"python",
    "idioma":"español",
    "programador":"santiago",
    "fecha":"2/09/2025",
    "usuarios":[
        {"nombre":"carlos","correo":"cdd@rr.com"},
        {"nombre":"felipe","correo":"cdd@rr.com"},
        {"nombre":"maria","correo":"cdd@rr.com"}
    ]
}

#acceder a datos
print(diccionario["usuarios"][0]["correo"])

#guardar diccionario como JSON en una arhcivo en el PC
with open('miPrimerJSON.json','w') as jsonFile:
    json.dump(diccionario,jsonFile)
    jsonFile.close()


#leer un archivo .jason y obtener la información del diccionario
with open('miSegundoJSON.json') as jsonFile:
    diccionarioProductos = json.load(jsonFile)
    jsonFile.close()

print(diccionarioProductos)