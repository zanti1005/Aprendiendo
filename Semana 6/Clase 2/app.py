from flask import Flask, render_template, url_for

app = Flask(__name__)

class Task:
    def __init__(self, descripcion, dueDate):
        self.descripcion = descripcion
        self.dueDate = dueDate

    def __str__(self):
        return self.descripcion + " - " + self.dueDate
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

    def endTask(self):
        if len(self.taskList)>0:
            self.currentTask = self.taskList.pop(0)
        else:
            self.currentTask = ''

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ruta2")
def ruta2():
    return "hola soy la ruta 2"

if __name__ == "__main__":
    app.run(debug=True)

