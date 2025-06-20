#hacer una lcase navegador con una lista de paginas visitadas
#hacer un metodo para navegar a una nueva página
#hacer un método para conocer el historial completo
#hacer un método para regresar a la página anterior
#cuando el navedador va hacia la página anterior 
# pierde la información de la página actual

#1. crear una clase navegador, uqe tenga dos atributos:
    #pagina actual
    #lista de páginas


class Navegador:
    def __init__(self, paginaInicial):
        self.paginaActual = paginaInicial
        self.listaDePaginas = []

    #2. método para navegar a una nueva página
    def navegar(self):
        #pedir la URL de la página de la que se quiere navegar
        url = input("Ingrese la página a la que quiere ingresar: ")
        #agragar la página actual al stack
        self.listaDePaginas.append(self.paginaActual)
        # actualizar la página acual al navegador
        self.paginaActual = url
    
    #3. medoto para regresar página anterior
    def regresar(self):
        #obtener la última página a la que se había navegado
        ultimaPagina = self.listaDePaginas.pop()
        self.paginaActual = ultimaPagina
 

navegador = Navegador("www.google.com")

while True:
    operaciones = """
        Ingrese N para navegar a una nueva página
        Ingrese H para conocer el historial completo
        Ingrese B para regresar a la página anterior
"""
    inputUsuario = input(operaciones)
    if inputUsuario == "N":
        navegador.navegar()
    elif inputUsuario == "H":
        print("Página actual: ", navegador.paginaActual)
        print("Historial anterior: ", navegador.listaDePaginas)
    elif inputUsuario == "B":
        navegador.regresar()
        print("Página actual: ", navegador.paginaActual)
