class Estadistica():

    #Metodo Constructor
    def __init__(varClase):
        varClase.x = []

    def agregar(varClase, valor):
        varClase.x.append(valor)

    def quitar(varClase, posicion):
        if posicion in range(1, len(varClase.x)):
            del varClase.x[posicion-1]
            return True
        else:
            return False

    def listar(varClase):
        texto = ""
        if len(varClase.x)>0:
            texto="Los datos son:\n"
            for i in range(0, len(varClase.x)):
                texto += "dato [" + str(i + 1) + "]=" + str(varClase.x[i]) + "\n"
        else:
            texto = "No hay datos"
        return texto

    def sumatoria(varClase):
        suma = 0
        for i in range(0, len(varClase.x)):
            suma += varClase.x[i]
        return suma

    def promedio(varClase):
        p = 0
        if len(varClase.x)>0:
            p = varClase.sumatoria() / len(varClase.x)
        return p

    def desviacion(varClase):
        d = 0
        if len(varClase.x)>1:
            p = varClase.promedio()
            s = 0
            for i in range(0, len(varClase.x)):
                s += abs(varClase.x[i] - p)        #abs es el valor absoluto
            d = s / (len(varClase.x) - 1)
        return d


# Subprograma que permite leer una variable númerica
# además de validar que el dato leido sea un número real
# repita la instrucción en caso de
def leerNumero(texto):
    numero = 0
    numeroValido = False

    while numeroValido == False:
        try:
            numero = float(input(texto))
            numeroValido = True
        except Exception as e:
            print("El dato no es numerico! error->[ ", e, " ]")
    return numero


#******************* Programa Principal ***************************

#Instanciar Objeto de la clase estadistica
objE = Estadistica()

#Crear menu
opcionMenu = 0
while opcionMenu != 7:
    print("--------------------")
    print("==== Menú Estadístico ====")
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
        objE.agregar(dato)

    elif opcionMenu == 2:
        p = int(leerNumero("Posicion a eliminar: "))
        if objE.quitar(p):
            print("El dato en la posicion ", p, " fue eliminado")
        else:
            print("Posicion no valida")

    elif opcionMenu == 3:
        print(objE.listar())

    elif opcionMenu == 4:
        print("la sumatoria es ", objE.sumatoria())

    elif opcionMenu == 5:
        print("el promedio es ", objE.promedio())

    elif opcionMenu == 6:
        print("la desviación estandar es ", objE.desviacion())

    elif opcionMenu != 7:
        print("Opción no valida")

print("La aplicación ha terminado")