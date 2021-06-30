from tkinter import *
import Util
import csv

nombreArchivo = "Ciudades.csv"
campos = ["Departamento", "Municipio"]
#Objeto tabla para despliegue de los datos
tMpios = None

def obtenerDeptos():
    global nombreArchivo, deptos
    deptos = []
    with open(nombreArchivo, newline="", encoding="utf8") as archivoCSV:
        registros = csv.DictReader(archivoCSV, fieldnames=campos, delimiter=";")
        #Variable semaforo
        anteriorDepto = ""
        for r in registros:
            if r[campos[0]] != anteriorDepto:
                #Cambiar variable semaforo
                anteriorDepto = r[campos[0]]
                deptos.append(anteriorDepto)

def obtenerMpios(e):
    global nombreArchivo, deptos, campos, tMpios
    #Verificar que haya depto seleccionado
    if cmbDepto.current():
        depto = deptos[cmbDepto.current()]

        with open(nombreArchivo, newline="", encoding="utf8") as archivoCSV:
            registros = csv.DictReader(archivoCSV, fieldnames=campos, delimiter=";")

            #Buscar el depto
            r = registros.__next__()
            while r[campos[0]] != depto:
                r = registros.__next__()

            datos = []
            #Agregar los mpios del depto
            while r[campos[0]] == depto:
                fila = []
                fila.append(r[campos[1]])
                r = registros.__next__()

            tMpios = Util.mostrarTabla(frm, ["Municipios"], datos, tMpios)


v = Tk()

v.minsize(300, 200)
deptos = obtenerDeptos()

Util.agregarEtiqueta(v, "Departamento", 0, 0)
cmbDepto = Util.agregarLista(v, deptos, 0, 1)

cmbDepto.bind("<<ComboboxSelected>>", obtenerMpios)

frm = Frame(v)
frm.grid(row=1, column=0, columspan=2)

v.mainloop()

