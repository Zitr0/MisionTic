# Elabore programa en Python que imprima la suma de los números enteros de -200 hasta 600

print("Programa para sumar los números desde un valor inicial hasta un valor final")

#valorInicial = int(input("Ingresar el valor Inicial: "))
#valorFinal = int(input("Ingresar el valor Final: "))

valorInicial = -200
valorFinal = 600

 #Proceso
valorAcumulado = 0
for i in range(valorInicial, valorFinal + 1):
    valorAcumulado += i

print("La suma desde: ", valorInicial, " hasta ", valorFinal, " es: ", valorAcumulado )