#Subprograma recursivo par el calculo del factorial
def obtenerFactorial(n):
    if n<=1:
        return 1
    else:
        return n * obtenerFactorial(n-1)

print("Programa para calcular el factorial de un numero")
numero = int(input("Ingresar el numero a calcular: "))

print("El factorial es", obtenerFactorial(numero))

#Solucion con ciclo
f = 1
for i in range(2, numero+1):
    f *= i

print("El factorial es", f)

def sumatoria(v, n):
    if n == 0:
        return v[n]
    else:
        return v[n] + sumatoria(v, n-1)

vector = [15, 12, 75, 30, 11]

s = 0
for v in vector:
    s += v

print("La sumatoria es", sumatoria(vector, len(vector)-1))
print("La sumatoria es", s)