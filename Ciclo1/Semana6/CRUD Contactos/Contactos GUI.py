from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Notebook
import Util

from Contacto import Contacto

#Lista de imágenes para los botones
iconos = ["./iconos/agregar.png", \
          "./iconos/editar.png", \
          "./iconos/eliminar.png", \
          "./iconos/guardar.png", \
          "./iconos/ordenar.png", \
          "./iconos/aceptar.png", \
          "./iconos/cancelar.png", \
          ]

<<<<<<< HEAD
#Lista de tooltips para los botones
textosTooltip = [ "Agregar Contacto", \
                  "Modificar Contacto", \
                  "Quitar Contacto", \
                  "Guardar cambios",\
                  "Ordenar lista", \
                  "Aceptar cambios", \
                  "Cancelar edición"
                  ]

=======
>>>>>>> main
#posiciones de los botones de edición para habilitarlos/deshabilitarlos
indiceBA = 5
indiceBC = 6

#Lista de encabezados de la tabla de datos
encabezados = ["ID", \
               "Nombre", \
               "Correo", \
               "Móvil"
               ]
#lista de paneles: Panel de lista y panel de edición
paneles = []
#Objeto tabla para despliegue de los datos
tContactos = None

#subrutina que cambia el ambiente de LISTAR a EDITAR y viceversa
def habilitar(editando):
    global indiceBA, indiceBC
    #Cambiar el estado de los botones
    for i in range(0, len(botones)):
        if editando:
            if i!=indiceBA and i!=indiceBC:
                botones[i].configure(state=DISABLED)
            else:
                botones[i].configure(state=NORMAL)
        else:
            if i!=indiceBA and i!=indiceBC:
                botones[i].configure(state=NORMAL)
            else:
                botones[i].configure(state=DISABLED)
    #Desplegar el panel respectivo
    if len(nb.tabs())>0:
        nb.forget(0)    #Limpiar las pestañas
    if editando:
        nb.add(paneles[1], text="Editando Contacto")
    else:
        nb.add(paneles[0], text="Lista de contactos")
    nb.focus()     #Refrescar las pestañas

#Metodo que muestra los contactos en una tabla
def mostrar():

<<<<<<< HEAD
    global tContactos
    datos = Contacto.pasarMatriz()
    tContactos = Util.mostrarTabla(paneles[0], encabezados, datos, tContactos)
=======
    datos = Contacto.pasarMatriz()
    Util.mostrarTabla(paneles[0], encabezados, datos, tContactos)
>>>>>>> main


#Método para limpiar los objetos de la edicion de un Contacto
def limpiar():
    #Dejar los controles vacíos
    txtId.Text = ""
    txtNombre.Text = ""
    txtCorreo.Text = ""
    txtMovil.Text = ""
    paneles[1].Text = "Editando datos de un nuevo Contacto"

#Metodo para ir a la edición de un registro
def iniciarEdicion():
    habilitar(True)
    #Se esta editando un Contacto existente?
    if Contacto.indice >= 0:
        c = Contacto.contactos[Contacto.indice]
        if c != None:
            Util.mostrar(txtId, c.id, False)
            Util.mostrar(txtNombre, c.nombre, False)
            Util.mostrar(txtCorreo, c.correo, False)
            Util.mostrar(txtMovil, c.movil, False)
            paneles[1].Text = "Editando datos del Contacto [" + c.nombre + "]"
    else:
        limpiar()

def agregar():
<<<<<<< HEAD
    Contacto.indice = -1
    iniciarEdicion()
    
def modificar():
    if tContactos.selection():
        Contacto.indice = tContactos.index(tContactos.selection())
        iniciarEdicion()
    else:
        messagebox.showinfo("", "No tiene ningún contacto seleccionado")
=======
    pass
    
def modificar():
    pass
>>>>>>> main

def eliminar():
    pass

def guardar():
    pass

def ordenar():
    pass

def aceptar():
<<<<<<< HEAD
    #Verificar si estoy agregando
    if Contacto.indice == -1:
        if txtId.get() != '' and txtNombre.get() != '' and txtCorreo.get() != '' and txtMovil.get() != '':
            Contacto.agregar(txtId.get(), \
                             txtNombre.get(), \
                             txtCorreo.get(), \
                             txtMovil.get())
            messagebox.showinfo("", "Contacto agregado al final de la lista")
        else:
            messagebox.showinfo("", "Faltan datos")
            habilitar()
    else:
        Contacto.modificar(txtId.get(), \
                         txtNombre.get(), \
                         txtCorreo.get(), \
                         txtMovil.get())

    #Volver al modo de listado
    habilitar(False)
    mostrar()

def cancelar():
    limpiar()
    # Volver al modo de listado
    mostrar()

=======
    pass

def cancelar():
    pass
>>>>>>> main

#Construir interfaz gráfica
v = Tk()
v.title("Mis contactos")
<<<<<<< HEAD
botones = Util.agregarBarra(v, iconos, textosTooltip) #Agrega una barra de herramientas
=======
botones = Util.agregarBarra(v, iconos) #Agrega una barra de herramientas
>>>>>>> main
nb = Notebook(v)
nb.pack(fill=BOTH, expand=YES)

paneles.append(Frame(v)) #panel de listado
paneles.append(Frame(v)) #panel de edición

#Objetos para editar un Contacto
Util.agregarEtiqueta(paneles[1], "ID:", 0, 0)
Util.agregarEtiqueta(paneles[1], "Nombre:", 1, 0)
Util.agregarEtiqueta(paneles[1], "Correo", 2, 0)
Util.agregarEtiqueta(paneles[1], "Móvil", 3, 0)
txtId=Util.agregarTexto(paneles[1], 15, 0, 1)
txtNombre=Util.agregarTexto(paneles[1], 30, 1, 1)
txtCorreo=Util.agregarTexto(paneles[1], 30, 2, 1)
txtMovil=Util.agregarTexto(paneles[1], 30, 3, 1)

#Comenzar con el despliegue de los datos
<<<<<<< HEAD
=======

>>>>>>> main
habilitar(False)
Contacto.obtener("Contactos.txt")
mostrar()

<<<<<<< HEAD
#Agregar los eventos asociados a los botones
botones[0].configure(command=agregar)
botones[1].configure(command=modificar)

botones[5].configure(command=aceptar)
botones[6].configure(command=cancelar)

=======
>>>>>>> main
v.mainloop()


