#Importar libreria para generar numeros aleatorios
import random

#importar libreria para interfaces graficas
from tkinter import *

from Enumerado import *

class Carta():

    #Metodo constructor
    def __init__(varClase):
        #Generar numero aleatorio entre 1 y 52
        varClase.indice = random.randrange(1, 53)

    def obtenerPinta(varClase):
        if varClase.indice <= 13:
            return PintaCarta.TREBOL

        elif varClase.indice <= 26:
            return PintaCarta.PICA

        elif varClase.indice <= 39:
            return PintaCarta.CORAZON

        else:
            return PintaCarta.DIAMANTE

    def mostrar(varClase, frm, x, y):
        lbl = Label(frm)

        img = PhotoImage(file=".\Cartas\Carta" + str(varClase.indice) + ".gif")
        lbl.config(image=img)
        lbl.image = img
        lbl.place(x=x, y=y)

    def obtenerIndiceNumero(varClase):
        n = varClase.indice % 13
        if n == 0:
            n = 13
        return n
