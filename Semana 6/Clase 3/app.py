from flask import Flask, render_template, url_for, redirect, request


app = Flask(__name__)

class Task:
    def __init__(self, description, dueDate):
        self.description = description
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

user =User("Daniel")

@app.route("/")
def index():
    return render_template('index.html', user=user, currentTask=user.currentTask)

@app.route("/add-task", methods=["GET","POST"])
def addTask():
    if request.method == "GET":
        return render_template('taks.html')
    elif request.method == "POST":
        print(request.form)
        description = request.form["description"]
        date = request.form["date"]
        newTask = Task(description,date)
        user.addTask(newTask)
        return redirect("/")


@app.route("/end-task", methods=["GET","POST"])
def endTask():
    user.endTask()
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)

