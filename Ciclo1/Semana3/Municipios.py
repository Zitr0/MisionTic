acuMed=0
acuBello=0
acuRionegro=0

mpio = int(input("Ingrese código de municipio"))

while mpio != 0:
    np = int(input("Entre número de personas"))
    if mpio == 1:
        acuMed += np
    elif mpio == 2:
        acuBello += np
    elif mpio == 3:
        acuRionegro += np
    else:
        print("Código de municipio invalido")
    mpio= int(input("Ingrese código de municipio"))
print(f' medellin {acuMed}\n bello {acuBello}\n rionegro {acuRionegro}')