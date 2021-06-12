import math


def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

def esPrimo(n):
    if n % 2 == 0:
        return False
    i = 3
    while i <= math.sqrt(i):
        if n % 1 == 0:
            return False
        i = i + 2
    return True

#Digito con el que comienza un numero
def comienzaCon(x):
    pd = x
    while pd > 9:
        pd = pd // 10
    return pd

#Maximo comun divisor
def mcd(x,y):
    res = x % y
    while res != 0:
        x = y
        y = res
        res = x % y
    return y


#Minimo comun multiplo
#se calcula como el producto de los numeros divido por su maximo comun divisor
def mcm(x, y):
    return x * y // mcd(x, y)
