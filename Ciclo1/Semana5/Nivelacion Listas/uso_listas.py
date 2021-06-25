from lista_ligada import *


a = LSL()

d = input("Ingrese el primer dato: ")
a.agregarDato(d)

"""
El ciclo for:
    Para usar buscarDondeInsertar, se debe tener una lista ligada
    que no esté vacia y luego buscarDondeInsertar(d) obtiene la
    posición de los elementos de menor a mayor
    o en orden alfabético, para luego ser insertados
"""

for i in range(1, 15):
    d = input("Ingrese el dato: ")
    y = a.buscarDondeInsertar(d)  
    a.insertar(d, y)

d = input("Ingrese más datos: ")

"""
El ciclo while agrega los datos al final de la lista
"""
while d != "0":
    a.agregarDato(d)
    d = input("Ingrese más datos: ")
    
# %%
print("\nLista ingresada: ")
a.recorrerLista()
print("\nlongitud: ", a.longitud())

#%%
"""
Procedimiento para borrar un nodo determinado.
"""
print()
y = nodoSimple()
x = a.buscarDato("1", y)
a.borrar(x, y)
print("despues de borrar la p")
a.recorrerLista()
print("\nlongitud: ", a.longitud())

#%%
"""
Procedimiento para borrar el primer nodo
"""

print()
x = a.primerNodo()
a.borrar(x)
print("despues de borrar el primer nodo")
a.recorrerLista()
print("\nlongitud: ", a.longitud())

#%%
"""
Procedimiento para borrar el último nodo
"""

print()
dat=a.ultimo.dato
y = nodoSimple()
x = a.buscarDato(dat, y)
a.borrar(x, y)
print("despues de borrar la p")
a.recorrerLista()
print("\nlongitud: ", a.longitud())

#%%
"""
Otro procedimiento para borrar el último nodo
"""

a.borrar_ultimo()
a.recorrerLista()

#%%
"""
Pilas y colas

"""
from lista_ligada import *

#%%

p=pila()
p.apilar("A")
p.apilar("B")
p.apilar("C")
p.apilar("D")
p.recorrerLista()

#%%
p.desapilar()
p.desapilar()
p.recorrerLista()

#%%
c=cola()
c.encolar("A")
c.encolar("B")
c.encolar("C")
c.encolar("D")
c.recorrerLista()
#%%
c.desencolar()
c.desencolar()
c.recorrerLista()

