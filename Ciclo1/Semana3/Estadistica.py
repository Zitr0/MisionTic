def sumatoria(datos):
    suma = 0
    for i in range(0, len(datos)):
        suma += datos[i]
    return suma

def promedio(datos):
    p = 0
    if len(datos)>0:
        p = sumatoria(datos) / len(datos)
    return p

def desviacion(datos):
    d = 0
    if len(datos)>1:
        p = promedio(datos)
        s = 0
        for i in range(0, len(datos)):
            s += abs(datos[i] - p)        #abs es el valor absoluto
        d = s / (len(datos) - 1)
    return d


def leerNumero(texto):
    numero = 0
    numeroValido = False

    while numeroValido == False:
        try:
            numero = float(input(texto))
            numeroValido = True
        except:
            print("El dato no es numerico!")
    return numero


#******************* Programa Principal ***************************
#Crear menu
x = []
opcionMenu = 0

while opcionMenu != 7:
    print("--------------------")
    print("Menu Opciones")
    print("1. Agregar dato ")
    print("2. Quitar dato ")
    print("3. Listar ")
    print("4. Sumatorio")
    print("5. Promedio ")
    print("6. Desviación Estandar ")
    print("7. Salir ")
    print("--------------------")
    opcionMenu = leerNumero("Opcion escogida: ")

    if opcionMenu == 1:
        dato = leerNumero("Valor a Agregar: ")
        x.append(dato)

    elif opcionMenu == 2:
        p = int(leerNumero("Posicion a eliminar: "))
        if p in range(1, len(x)):
            del x[p-1]
            print("El dato en la posicion ", p, " fue eliminado")
        else:
            print("Posicion no valida")

    elif opcionMenu == 3:
        if len(x)>0:
            for i in range(0, len(x)):
                print("dato [", str(i + 1), "]=", x[i])
        else:
            print("No hay datos")

    elif opcionMenu == 4:
        print("la sumatoria es ", sumatoria(x))

    elif opcionMenu == 5:
        print("el promedio es ", promedio(x))

    elif opcionMenu == 6:
        print("la desviación estandar es ", desviacion(x))

    elif opcionMenu != 7:
        print("Opción no valida")

print("La aplicación ha terminado")
