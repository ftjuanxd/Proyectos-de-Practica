import pickle
import os

#esta ruta solo funciona si desde la terminal nos ubicamos en la carpeta del gestor de tareas de lo contrario da error

route_file_task = "./assets/task.pkl"



class Task:

    def __init__(self,name,description,state):
        self.name = name
        self.description = description
        self.state = state # Si el estado no se proporcionar el valor por defecto sera "Not Started"

    def __repr__(self):
        return f"Tarea: {self.name}.\n Descripcion: {self.description}.\n Estado: {self.state}.\n"


#File's Functions
def file_test():
    if os.path.exists(route_file_task):
        return True
    else:
        return False

#Save Task
def save_task(task:list):
    if file_test():
        with open (route_file_task,"ab") as archivo:
            pickle.dump(task,archivo)
        return "Task Saved"
    else:
        return "File not Found"

#Read Task
def read_task():
    saved_task= list()
    if file_test():
        with open(route_file_task,"rb") as archivo:
            while True:
                try:
                    saved_task.append(pickle.load(archivo))
                except EOFError:
                    break
    else:
        return "File not Found"
    
    for task in saved_task:
            print(task)
    
def get_route():
    current_directory = os.getcwd()

    route_file_task = os.path.join(current_directory,"assets","task.pkl")

    print(route_file_task)
