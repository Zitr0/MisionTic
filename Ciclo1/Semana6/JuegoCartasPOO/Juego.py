#importar libreria para interfaces graficas
from tkinter import *

#Importar caja de mensajes
from tkinter import messagebox

#Importar libreria para pestañas
from tkinter.ttk import Notebook

#crear ventana
v = Tk()
v.title("Juego del apuntado")
v.minsize(width=500, height=500)

#Crear el menu principal
mnuP = Menu(v)
#Agregar a la ventana
v.config(menu=mnuP)

def repartir():
    messagebox.showinfo("Probando menu", "Hizo click en repartir")

def verificar():
    messagebox.showinfo("Probando menu", "Hizo click en verificar")

def salir():
    v.destroy()
    quit()

#Opciones del menu
mnuJ = Menu(mnuP)
mnuJ.add_command(label="Repartir", command=repartir)
mnuJ.add_command(label="Verificar", command=verificar)
mnuP.add_cascade(label="Juego", menu=mnuJ)

mnuP.add_command(label="Salir", command=salir)

#Definir las pestañas del juego
nbJ = Notebook(v)
nbJ.pack(fill="both", expand="yes")  #Para ocupar toda la ventana

f1 = Frame(nbJ, bg="green")
f2 = Frame(nbJ, bg="lightblue")

nbJ.add(f1, text="Jugador 1")
nbJ.add(f2, text="Jugador 2")

v.mainloop()
