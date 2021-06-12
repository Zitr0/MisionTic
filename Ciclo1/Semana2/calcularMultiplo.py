print("Programa para calcular el multiplo de un número")

valorMultiplo = int(input("Ingresar el valor del que quiere sumar los multiplos: "))
valorLimite = int(input("Ingresar el valor limite: "))


if valorMultiplo > 0 and valorLimite >= valorMultiplo:

    #Proceso
    valorAcumulado = 0
    for i in range(1, valorLimite + 1):
        if i % valorMultiplo == 0:
            valorAcumulado += i
else:
    print("Los datos no son validos")

print("La suma de los multiplos de: ", valorMultiplo, " hasta ", valorLimite, " es: ", valorAcumulado )

