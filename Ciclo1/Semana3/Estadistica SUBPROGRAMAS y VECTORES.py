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
            s += abs(datos[i] - p)
        d = s / (len(datos) - 1)
    return d

def leerNumero(mensaje):
    numero = 0
    numeroValido = False
    while not numeroValido:
        try :
            numero = float(input(mensaje))
            numeroValido = True
        except:
            print("El dato no es numérico!")
    return numero

x = []
opcionMenu = 0
while opcionMenu != 7:
    print("1. Agregar dato")
    print("2. Quitar dato")
    print("3. Listar")
    print("4. Sumatoria")
    print("5. Promedio")
    print("6. Desviacion Estandar")
    print("7. Salir")

    opcionMenu = leerNumero("Opcion escogida?")

    if opcionMenu == 1:
        dato = leerNumero("Valor a agregar?")
        x.append(dato)
    elif opcionMenu == 2:
        p = int(leerNumero("Posición a quitar?"))
        if p in range(1, len(x)+1):
            del x[p-1]
            print("El dato en la posición ",p, " fue quitado")
        else:
            print("Posición no valida")
    elif opcionMenu == 3:
        if len(x)>0:
            for i in range(0, len(x)):
                print("dato [",str(i+1),"]=", x[i])
        else:
            print("No hay datos")
    elif opcionMenu == 4:
        print("La sumatoria es: ", sumatoria(x))
    elif opcionMenu == 5:
        print("El promedio es: ", promedio(x))
    elif opcionMenu == 6:
        print("La desviación estandar es: ", desviacion(x))
    elif opcionMenu != 7:
        print("Opcion no válida")

        
        
