'''
Elabore un programa en Python que lea un entero de dos dígitos y produzca como salida los dígitos
del número leído con su correspondiente mensaje.
Por ejemplo, si el número leído es 27, la salida deberá ser:(sin texto adicional):
2
7
'''

enteroDosDigitos = int(input("Ingrese un entero de dos digitos: "))
uno = (enteroDosDigitos // 10)
dos = enteroDosDigitos % 10

print(uno,'\n', dos)