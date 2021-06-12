valorInicial = int(input("Ingrese el valor inicial entero "))

factorial = 1
i = 1
while i <= valorInicial:
    factorial = factorial * i
    i = i +1
print("El factorial de: ", valorInicial, " es ",factorial)