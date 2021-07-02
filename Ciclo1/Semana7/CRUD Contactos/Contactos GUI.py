from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Notebook
import Util

import time

from Contacto import Contacto

#Lista de imágenes para los botones
iconos = ["./Iconos/Agregar.png", \
          "./Iconos/Editar.png", \
          "./Iconos/Eliminar.png", \
          "./Iconos/Guardar.png", \
          "./Iconos/Ordenar.png", \
          "./Iconos/OrdenarRapido.png", \
          "./Iconos/Aceptar.png", \
          "./Iconos/Cancelar.png"
          ]
textosBotones = ["agregar contacto", \
                 "modificar contacto", \
                 "eliminar contacto", \
                 "guardar cambios", \
                 "ordenar los contactos", \
                 "ordenar rápido los contactos", \
                 "aceptar cambios", \
                 "cancelar los cambios"
                 ]

#posiciones de los botones de edición para habilitarlos/deshabilitarlos
indiceBA = 6
indiceBC = 7

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
        nb.forget(0)
    if editando:
        nb.add(paneles[1], text="Editando Contacto")
    else:
        nb.add(paneles[0], text="Lista de contactos")
    nb.focus()

#Metodo que muestra los contactos en una tabla
def mostrar():
    global tabla, encabezados, tContactos
    datos = Contacto.pasarMatriz()
    tContactos = Util.mostrarTabla(paneles[0], \
                                    encabezados, \
                                    datos, \
                                    tContactos)

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
        c = Contacto.obtenerActual()
        if c != None:
            Util.mostrar(txtId, c.id, False)
            Util.mostrar(txtNombre, c.nombre, False)
            Util.mostrar(txtCorreo, c.correo, False)
            Util.mostrar(txtMovil, c.movil, False)
            paneles[1].Text = "Editando datos del Contacto [" + c.nombre + "]"
    else:
        limpiar()

def agregar():
    Contacto.indice = -1;
    iniciarEdicion()
    
def modificar():
    global tContactos
    if tContactos.selection():
        #Indice del Contacto a editar
        Contacto.indice = tContactos.index(tContactos.selection())
        #Iniciar los controles
        iniciarEdicion()
    else:
        messagebox.showerror("Editando Contacto", "Debe seleccionar un Contacto")

def eliminar():
    global tContactos
    if tContactos.selection():
        decision = messagebox.askquestion("Eliminando Contacto", "Está seguro?")
        if decision == "yes":
            #Indice del Contacto a eliminar
            Contacto.indice = tContactos.index(tContactos.selection())
            #Realizar el retiro del registro y actualizar la lista
            contactos = Contacto.eliminar()
            mostrar()
            messagebox.showerror("Eliminando Contacto", "El Contacto fue eliminado");
    else:
        messagebox.showerror("Eliminando Contacto", "Debe seleccionar un Contacto")

def guardar():
    Contacto.guardar("Contactos.json")
    messagebox.showinfo("Guardando cambios", "Se guardaron los cambios en el archivo")

def ordenar():
    inicio = time.time()
    Contacto.ordenar()
    fin = time.time()
    duracion = fin - inicio
    etiquetas[0]["text"]="Demora ordenar:"+"{0:,.5f}".format(duracion)+"segundos"
    mostrar()

def ordenarRapido():
    inicio = time.time()
    Contacto.ordenarRapido()
    fin = time.time()
    duracion = fin - inicio
    etiquetas[1]["text"]="Demora ordenar rápido:"+"{0:,.5f}".format(duracion)+"segundos"
    mostrar()

def aceptar():
    if Contacto.indice == -1:
        #se esta agregando un contacto
        Contacto.agregar(txtId.get(), \
                         txtNombre.get(), \
                         txtCorreo.get(), \
                         txtMovil.get())
    else:
        #Se esta modificando un contacto
        Contacto.modificar(txtId.get(), \
                         txtNombre.get(), \
                         txtCorreo.get(), \
                         txtMovil.get())
    habilitar(False)
    mostrar()

def cancelar():
    habilitar(False)

#Construir interfaz gráfica
v = Tk()
v.title("Mis contactos")
botones = Util.agregarBarra(v, iconos, textosBotones) #Agrega una barra de herramientas

etiquetas = Util.agregarBarraEstado(v, 2)
etiquetas[0]["text"]="Demora ordenar"
etiquetas[1]["text"]="Demora ordenar rápido"

nb = Notebook(v)
nb.pack(fill=BOTH, expand=YES)

paneles.append(Frame(v)) #panel de listado
paneles.append(Frame(v)) #panel de edición

#Objetos para editar un Pais
Util.agregarEtiqueta(paneles[1], "ID:", 0, 0)
Util.agregarEtiqueta(paneles[1], "Nombre:", 1, 0)
Util.agregarEtiqueta(paneles[1], "Correo", 2, 0)
Util.agregarEtiqueta(paneles[1], "Móvil", 3, 0)
txtId=Util.agregarTexto(paneles[1], 15, 0, 1)
txtNombre=Util.agregarTexto(paneles[1], 30, 1, 1)
txtCorreo=Util.agregarTexto(paneles[1], 30, 2, 1)
txtMovil=Util.agregarTexto(paneles[1], 30, 3, 1)

#eventos para los botones de la barra
botones[0].configure(command=agregar)
botones[1].configure(command=modificar)
botones[2].configure(command=eliminar)
botones[3].configure(command=guardar)
botones[4].configure(command=ordenar)
botones[5].configure(command=ordenarRapido)
botones[6].configure(command=aceptar)
botones[7].configure(command=cancelar)

#Iniciar listando los contactos
Contacto.obtener("Contactos.json")
habilitar(False)
mostrar()

v.mainloop()

