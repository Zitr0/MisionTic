#Importar libreria para generar numeros aleatorios
import random

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