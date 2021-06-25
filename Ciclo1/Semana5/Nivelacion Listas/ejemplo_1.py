from lista_ligada import *

nodo1 = nodoSimple("H")
nodo2 = nodoSimple("O")
nodo3 = nodoSimple("L")
nodo4 = nodoSimple("A")

nodo1.asignarLiga(nodo2)
nodo2.asignarLiga(nodo3)
nodo3.asignarLiga(nodo4)

#print(nodo1.retornarDato())
siguiente = nodo1.liga
#print(siguiente.retornarDato())


siguiente = siguiente.liga
#print(siguiente.retornarDato())

siguiente = siguiente.liga
#print(siguiente.retornarDato())

siguiente=nodo1

while siguiente != None:
    print(siguiente.retornarDato())
    siguiente = siguiente.liga







'''
nodo1=nodoSimple("Hola, ")
nodo2 = nodoSimple("¿Cómo ")
nodo3=nodoSimple("estas ")


nodo4=nodoSimple("tú?")

## Ligo el nodo 1 con el nodo 2
nodo1.asignarLiga(nodo2)
nodo2.asignarLiga(nodo3)
nodo3.asignarLiga(nodo4)

print(nodo1.dato, end="")
nuevaLiga = nodo1.liga

while nuevaLiga != None:
    
    print(nuevaLiga.dato, end="")
    
    nuevaLiga = nuevaLiga.liga
'''


