import random
from tkinter import *

class Dado():

    #Metodo constructor
    def __init__(varClase):
        varClase.numero = 1

    def lanzar(varClase):
        #generar al azar un valor entre 1 y 6
        varClase.numero = random.randrange(1, 7)

    def obtenerNumero(varClase):
        return varClase.numero

    def mostrar(varClase, lbl):
        #Cargar la imagen, con un objeto PHOTOIMAGE
        img = PhotoImage(file=str(varClase.numero)+".png")

        #mostrar la imagen en la etiqueta  objeto LABEL
        lbl.config(image=img)
        lbl.image=img


