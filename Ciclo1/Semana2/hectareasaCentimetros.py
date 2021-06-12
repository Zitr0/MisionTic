'''
Elabore un programa en Python que lea un área en hectáreas
y la convierta en centímetros cuadrados y muestre el resultado con un mensaje bien explicativo.
'''

valorHectarea = float(input("Ingrese area en hectareas "))
valorHectarea = valorHectarea * 10000
valorCentimetros = valorHectarea * 10000
print("El area ", valorHectarea, " en centimetros cuadrados es ", valorCentimetros )