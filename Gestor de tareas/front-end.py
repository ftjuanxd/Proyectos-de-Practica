import os
import time
from backend import *

def show_menu():
        os.system("clear")
        print("\nBienvenido al gestor de tareas")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Marcar tarea como completada")
        print("5. Salir")

def main():
    task = []
    
    while True:
        show_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            read_task()
        elif opcion == "2":
            #Inputs
            nombre = input("Cual es el nombre de la nueva tarea:")
            descripcion = input("Cual es la descripcion de la nueva tarea: ")
            estado = input("Cual es el estado de la nueva tarea (no ejecutado/pendiente/completada): ")
            #Add task
            task.append(Task(nombre,descripcion,estado))
            save_task(task)
            #Check Process
            print("Logrado")
        elif opcion == "5":
             break
        else:
            print("Opción no válida. Intenta nuevamente.")
        
        time.sleep(2)

main()

#hacer una aplicacion de gestion de tareas donde el usuario pueda ver, agregar, eliminar y marcar como completada las tareas