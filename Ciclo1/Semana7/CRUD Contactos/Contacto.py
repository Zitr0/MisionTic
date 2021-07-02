import json

class Contacto:

    #posición del registro a editar
    indice = -1
    #lista de contactos
    contactos = []

    #Método constructor
    def __init__(varClase, id, \
                         nombre, \
                         correo, \
                         movil):
        varClase.id = id
        varClase.nombre = nombre
        varClase.correo = correo
        varClase.movil = movil

    def actualizar(varClase, id, nombre, correo, movil):
        varClase.id = id
        varClase.nombre = nombre
        varClase.correo = correo
        varClase.movil = movil

    def aJSON(varClase):
        return json.dumps(varClase, default=lambda c: c.__dict__, indent=4)

    #Obtener la lista de Contactos o un contacto en particular desde un archivo
    @staticmethod
    def obtener(nombreArchivo):
        with open(nombreArchivo) as archivoJSON:
            datos = json.load(archivoJSON)
            for d in datos:
                c = Contacto(d["id"], d["nombre"], d["correo"], d["movil"])
                Contacto.contactos.append(c)

    #Convertir los registros en una matriz de textos
    @staticmethod
    def pasarMatriz():
        datos = []
        for c in Contacto.contactos:
            fila = []
            fila.append(c.id)
            fila.append(c.nombre)
            fila.append(c.correo)
            fila.append(c.movil)
            datos.append(fila)
        return datos

    #Método para Agregar un Contacto
    @staticmethod
    def agregar(id, nombre, correo, movil):
        c = Contacto(id, nombre, correo, movil)
        Contacto.contactos.append(c)

    #Método para Modificar un Contacto
    @staticmethod
    def modificar(id, nombre, correo, movil):
        if Contacto.indice in range(0, len(Contacto.contactos)):
            Contacto.contactos[Contacto.indice].actualizar(id, nombre, correo, movil)

    #Método para Eliminar un Contacto
    @staticmethod
    def eliminar():
        if Contacto.indice in range(0, len(Contacto.contactos)):
            del Contacto.contactos[Contacto.indice]

    #Método para obtener el actual Contacto
    @staticmethod
    def obtenerActual():
        if Contacto.indice in range(0, len(Contacto.contactos)):
            return Contacto.contactos[Contacto.indice]
        else:
            return None

#Método para Ordenar la lista de Contactos
    @staticmethod
    def ordenar():
        for i in range(len(Contacto.contactos)-1):
            for j in range(i+1, len(Contacto.contactos)):
                if Contacto.contactos[i].nombre >= Contacto.contactos[j].nombre:
                    Contacto.intercambiar(i, j)

    #Metodo que intercambia los elementos i y j de la lista
    @staticmethod
    def intercambiar(i, j):
       Contacto.contactos[j], Contacto.contactos[i] = Contacto.contactos[i], Contacto.contactos[j]            

    #Método para Ordenar la lista de Contactos Metodo Rapido
    @staticmethod
    def ordenarRapido():
        Contacto._ordenarRapido(0, len(Contacto.contactos) - 1)

    #Metodo recursivo de ordenamiento
    #los índices inicio y fin indican sobre qué parte de la lista va operar
    def _ordenarRapido(inicio, fin):
       #Punto de finalización
       if inicio >= fin:
          return

       # Caso recursivo
       posicionPivote = Contacto.ubicarPivote(inicio, fin)
       Contacto._ordenarRapido(inicio, posicionPivote - 1)
       Contacto._ordenarRapido(posicionPivote + 1, fin)

    #Metodo que busca la posición pivote
    #donde todos los elementos por encima son mayores
    #y todos los elementos por debajo son posicionPivote
    def ubicarPivote(inicio, fin):
       pivote = Contacto.contactos[inicio].nombre
       posicionPivote = inicio

       # Cambia de lugar los elementos
       for i in range(inicio+1, fin + 1):
          if Contacto.contactos[i].nombre < pivote:
             posicionPivote += 1
             if i != posicionPivote:
                Contacto.intercambiar(i, posicionPivote)

       # Pone el pivote al final de los menores
       if inicio != posicionPivote:
          Contacto.intercambiar(inicio, posicionPivote)

       # Devuelve la posición del pivote
       return posicionPivote
                    

    #Método para Guardar los Contactos en un archivo
    @staticmethod
    def guardar(nombreArchivo):
        with open(nombreArchivo, "w") as archivoJSON:
            json.dump([c.__dict__ for c in Contacto.contactos], archivoJSON)

        #lineas = open(nombreArchivo, "w")
        #strJSON = json.dumps([c.__dict__ for c in Contacto.contactos])
        #lineas.write(strJSON)
        #lineas.close()
        

    
