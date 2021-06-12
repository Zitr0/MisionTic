#Cargar libreria GUI
from tkinter import * 

#Crear ventana
ventana = Tk()
ventana.title("Calculo semana santa")
ventana.minsize(300,200)

#Agregar etiqueta
Label(ventana, text="Año a Calcular:").grid(row=0, column=0)

#Agregar cajas de texto
txtAno =  Entry(ventana, width=10)
txtAno.grid(row=0, column=1)

txtFecha = Entry(ventana, width=30)
txtFecha.grid(row=1, column=1)
txtFecha.configure(state=DISABLED)

#Algoritmo
def obtenerSemanaSanta():
    #Obtener datos de entrada
    ano = int(txtAno.get())

    #Proceso
    a = ano % 19
    b = ano % 4
    c = ano % 7
    d = (19 * a + 24) % 30
    dias = d + (2*b + 4*c + 6*d + 5) % 7

    dia = 15 + dias
    mes = "Marzo"

    if dia > 31:
        dia = dia - 31
        mes="Abril"

    #mostrar los datos de salida
    
    txtFecha.configure(state=NORMAL)
    txtFecha.delete(0,END)
    txtFecha.insert(0, str(dia) + " de " + mes)
    txtFecha.configure(state=DISABLED)
    

#Agregar Boton
Button(ventana, text="Calcular", command=obtenerSemanaSanta).grid(row=1, column=0)

#Necesario para que aparezca la ventana
ventana.mainloop()