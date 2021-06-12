#Libreria para obtener datos XML
import xml.etree.ElementTree as datosXML

class Territorio():

    #Metodo constructor padre
    def __init__(varClase, valores):
        varClase.campos = ["Codigo", "Nombre"]
        varClase.valores = valores

    def obtenerRegistro(varClase):
        return dict(zip(varClase.campos, varClase.valores))

#Para heredar de otra clase se pone la clase padre en el parentesis
class Pais(Territorio):

    #Metodo constructor que altera el heredado
    def __init__(varClase, valores):
        super().__init__(valores)
        varClase.campos.append("CodigoAlfa2")
        varClase.campos.append("CodigoAlfa3")


    def obtener(codigo=""):
        # Abrir el documento XML
        dXML = datosXML.parse("Paises.xml")

        # Obtener la lista de nodos
        nodos = dXML.getroot()


        if codigo == "":
            lista = []
            # Mostrar la lista de nodos de manera OBJETUAL
            for n in nodos:
               p = Pais([ n.attrib["Codigo"], n.attrib["Nombre"], n.attrib["CodigoA2"], n.attrib["CodigoA3"]])
               lista.append(p)
            return lista
        else:
            #Buscar el pais que corresponda al código
            for n in nodos:
                if n.attrib["Codigo"] == codigo:
                    return Pais([ n.attrib["Codigo"], n.attrib["Nombre"], n.attrib["CodigoA2"], n.attrib["CodigoA3"]])
            return None

class Departamento(Territorio):

    def __init__(varClase, valores):
        super().__init__(valores)

    def obtener(codigo=""):
        # Abrir el documento XML
        dXML = datosXML.parse("Departamentos.xml")

        # Obtener la lista de nodos
        nodos = dXML.getroot()

        if codigo == "":
            #Obtener la lista de departamentos
            lista = []
            for n in nodos:
                lista.append(Departamento([ n.attrib["Codigo"], n.attrib["Nombre"] ]))
            return lista
        else:
            # Buscar el departamento que corresponda al código
            for n in nodos:
                if n.attrib["Codigo"] == codigo:
                    return Departamento([n.attrib["Codigo"], n.attrib["Nombre"]])
            return None

class Municipio(Territorio):

    def __init__(varClase, valores, codigoDepartamento):
        super().__init__(valores)
        varClase.departamento = Departamento.obtener(codigoDepartamento)

    def obtener(codigo="", codigoDepto=""):
        # Abrir el documento XML
        dXML = datosXML.parse("Municipios.xml")

        # Obtener la lista de nodos
        nodos = dXML.getroot()

        if codigo == "":
            # Obtener la lista de municipios
            lista = []
            for n in nodos:
                agregar = True
                if codigoDepto !="" and n.attrib["CodigoDepartamento"]!=codigoDepto:
                    agregar = False
                if agregar:
                    m = Municipio([n.attrib["CodigoMunicipio"], n.attrib["Nombre"]],\
                                  n.attrib["CodigoDepartamento"])
                    lista.append(m)
            return lista
        else:
            # Buscar el municipio que corresponda al código
            for n in nodos:
                if n.attrib["CodigoMunicipio"] == codigo:
                    return Municipio([n.attrib["CodigoMunicipio"], n.attrib["Nombre"]],\
                                     n.attrib["CodigoDepartamento"])
            return None

#Programa principal

codigo = input("Codigo del departamento a consultar: ")
depto = Departamento.obtener(codigo)

if depto != None:
    rd = depto.obtenerRegistro()
    print("Los municipios del depto ", rd["Nombre"], "Son:")
    #Obtener la lista de municipios para un departamento
    mpios = Municipio.obtener(codigoDepto=rd[""])
    for m in mpios:
        print(m.obtenerRegistro()["Nombre"])
else:
    print("No existe departamento con ese codigo")

