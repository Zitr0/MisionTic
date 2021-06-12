valorInicial = int(input("Ingrese el valor inicial entero "))

sumaEnteros = 0
i = 1
while i <= valorInicial:
    sumaEnteros = sumaEnteros + i
    i = i +1
print("La suma de los enteros desde ",valorInicial, " es ",sumaEnteros)

suma=0
#con For
for i in range(1, valorInicial+1,1):
    suma = suma + i
print("La suma de los enteros desde 1 hasta n, es",valorInicial, " es ",suma)
