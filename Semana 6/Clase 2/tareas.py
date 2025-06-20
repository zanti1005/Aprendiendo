#implementar un sistema de gestión de tareas
#un usuario debe tener un nombre, una lista de tareas y una tarea en curso
#los elementos de la lista de tareas son de una clase de tarea
#la clase Tarea tiene los siguientes atributos:
    #descripcion de la tarea
    #fecha límite de la tarea
#la clase usuario tiene los siguientes atributos:
    #nombre
    #tareaActual
    #listaTareas
#la clase usuario tiene los siguientes métodos:
    #agregar una tarea:
        #si el usuario no tiene tarea actual, la agrega como tarea actual
        #si el usuario ya tiene tarea actual, la agrega al final 
        # de la lista de tareas pendientes 
    #finalizar una tarea
        #saca la siguientes tarea de la lista y la pone en "tarea actual"

#1. hacer una clase tarea
class Task:
    def __init__(self, descripcion, dueDate):
        self.descripcion = descripcion
        self.dueDate = dueDate

    def __str__(self):
        return self.descripcion + " - " + self.dueDate
    
#2. hacer la clase usuario
class User:
    def __init__(self,name):
        self.name=name
        self.currentTask = ''
        self.taskList = []
    
    def addTask(self,newTask):
        #revisar si el usuario ya tiene una atrea actual
        if self.currentTask == '':
            self.currentTask = newTask
        else:
            self.taskList.append(newTask)

    def printTask(self):
        print("Tarea actual",self.currentTask)
        print("Lista de tareas: ")
        for task in self.taskList:
            print(task)

    def endTask(self):
        if len(self.taskList)>0:
            self.currentTask = self.taskList.pop(0)
        else:
            self.currentTask = ''
        print("Método para finalizar una tarea")

#3.hacer la lógica de la aplicación

user = User("Daniel")

while True:
    operaciones = """
        Ingrese A para registrar una nueva tarea
        Ingrese B para finalizar tarea actual
        Ingrese I para imprimir la lista de tarea
    """
    inputUsuario = input(operaciones)
    if inputUsuario == "A":
        #pedir a usuario descripcion de tarea y fecha límite
        descripcion = input("Por favor ingrese la descripción de la tarea: ")
        date = input("Por favor ingrese la fecha de la tarea: ")
        #crear tarea
        newTask = Task(descripcion,date)
        #implementarmétodo addTask de la clase user
        user.addTask(newTask)
    elif inputUsuario == "I":
        user.printTask()
    elif inputUsuario == "F":
        user.endTask()
        print("Finalizar la tarea actual")

