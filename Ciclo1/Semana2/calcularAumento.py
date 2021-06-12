nombre = input("Ingrese un nombre: ")

while nombre != "":
    salario = int(input(f"{nombre} ingrese salario: "))
    aumento = 0
    if salario < 1000:
        aumento = salario *0.1
    nuevoSalario = salario + aumento
    print("Nombre ", nombre, "\tsalario", salario, "\tAumento\t", aumento, "\tNuevo Salario\t", nuevoSalario)
    nombre = input("Ingrese un nombre: ")
print("Termine")