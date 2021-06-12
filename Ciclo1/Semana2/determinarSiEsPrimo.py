#determinar si un numero es primo o no

x = int(input("Ingrese un numero entero: "))
i = 2

while i <= x**(.5) and x % i !=0:
    i = i + 1
if i > x**(.5):     #Raiz cuadrada
    print(x, " es primo")
else:
    print(x, "No es primo, es divisible por ", i)

