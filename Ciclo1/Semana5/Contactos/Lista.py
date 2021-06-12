from Nodo import Nodo

class Lista():

    def __init__(varClase):
        varClase.cabeza = None

    #Metodo para agregar nodo a la lista
    def agregar(varClase, n):
        if n!= None:
            if varClase.cabeza == None:
                #La lista esta vacia
                #El nodo agregado es la cabeza
                varClase.cabeza = n
            else:
                #recorrer la lista hasta el ultimo nodo
                apuntador = varClase.cabeza
                while apuntador.siguiente != None:
                    apuntador = apuntador.siguiente
                apuntador.siguiente = n
                n.siguiente = None

    def desdeArchivo(varClase, nombreArchivo):
        varClase.cabeza = None
        lineas = open(nombreArchivo, "r")
        for linea in lineas:
            datos = linea.split(";")
            if len(datos) >= 4:
                n = Nodo(datos[1], datos[3], datos[2])
                varClase.agregar(n)

    def mostrar(varClase):
        # recorrer la lista hasta el ultimo nodo
        apuntador = varClase.cabeza
        while apuntador != None:
            print(apuntador.nombre, apuntador.correo)
            apuntador = apuntador.siguiente