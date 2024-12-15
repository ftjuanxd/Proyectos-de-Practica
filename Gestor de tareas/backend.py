import pickle
import os

#esta ruta solo funciona si desde la terminal nos ubicamos en la carpeta del gestor de tareas de lo contrario da error

route_file_task = "./assets/task.pkl"



class Task:

    message = "Error File Not Found"

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
        return Task.message

#Read Task
def read_task():
    if file_test():
        with open(route_file_task,"rb") as archivo:
            saved_task= list()
            while True:
                try:
                    saved_task.append(pickle.load(archivo))
                except EOFError:
                    break
            return saved_task
    else:
        return Task.message

def delete_task(name_task:str):
    tasks = read_task()
    if tasks == Task.message:
        return Task.message
    
    #Filtra por el medio del parametro que el usuario a eliminar y solo guarda los que sean diferentes
    tasks = [task for task in tasks if task.name != name_task]
    
    with open(route_file_task,"wb") as file:
        for task in tasks:
            pickle.dump(task,file)

    return f"The task with name: {name_task} was deleted."

def get_route():
    current_directory = os.getcwd()

    route_file_task = os.path.join(current_directory,"assets","task.pkl")

    print(route_file_task)
