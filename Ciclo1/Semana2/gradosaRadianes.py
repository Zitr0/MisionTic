'''
Elabore un programa en Python que lea un dato,
el cual es el valor de un ángulo en grados, y que lo convierta e imprima en radianes.
Use pi = 3.14
'''

pi = 3.14

valorGrados = float(input("Ingrese el valor en grados "))
valorRadianes = valorGrados * (pi/180)

print(valorRadianes)