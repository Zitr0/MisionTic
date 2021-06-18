n = 5

nomMpio = ["", "Medellin", "Rionegro", "Envigado", "La ceja", "El carmen"]
acmpio = [0]*(n+1)

mpio = int(input("Ingrese código de municipio "))

while mpio != 0:
    np = int(input("Ingrese número de personas "))
    acmpio[mpio]=acmpio[mpio]+np
    mpio = int(input("Ingrese código de municipio "))

for i in range(1, n + 1):
    if acmpio[i] != 0:
        print("Municipio ", nomMpio[i], "Habitantes ", acmpio[i])