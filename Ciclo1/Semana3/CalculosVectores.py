def sumaVector(V, n):
    s = 0
    for i in range(1, n):
        s += V[i]
    return s

def mayorDato(V, n):
    mayor = 0
    for i in range(n):
        if V[i] > V[mayor]:
            mayor = i
    return mayor

n = 6

nomMpio = ["", "Medellin", "Rionegro", "Envigado", "La ceja", "El carmen"]
acmpio = [0] * n

mpio = int(input("Ingrese código de municipio "))

while mpio != 0:
    np = int(input("Ingrese número de personas "))
    acmpio[mpio] = acmpio[mpio] + np
    mpio = int(input("Ingrese código de municipio "))

for i in range(1, n):
    if acmpio[i] != 0:
        print("Municipio ", nomMpio[i], "Habitantes ", acmpio[i])

totalHabitantes = sumaVector(acmpio, n)
print("El total de habitantes es ", totalHabitantes)

i = mayorDato(acmpio, n)
print("El mayor número de habitantes está en el municipio", end=" ")
print(nomMpio[i], "con", acmpio[i], "Habitantes")