#Calcular nota

nota1 = float(input("Ingresa valor para nota 1: "))
nota2 = float(input("Ingresa valor para nota 2: "))
nota3 = float(input("Ingresa valor para nota 3: "))
nota4 = float(input("Ingresa valor para nota 4: "))
nota5 = float(input("Ingresa valor para nota 5: "))

porcentajeNota1 = 15
porcentajeNota2 = 15
porcentajeNota3 = 20
porcentajeNota4 = 25
porcentajeNota5 = 25

nota1 = nota1 * (porcentajeNota1 /100)
nota2 = nota2 * (porcentajeNota2 /100)
nota3 = nota3 * (porcentajeNota3 /100)
nota4 = nota4 * (porcentajeNota4 /100)
nota5 = nota5 * (porcentajeNota5 /100)


sumaNotas = nota1 + nota2 + nota3 + nota4 + nota5
notaFinal = sumaNotas

print("Su nota 1 equivale a: ", porcentajeNota1, " es " , nota1)
print("Su nota 2 equivale a: ", porcentajeNota2, " es " , nota2)
print("Su nota 3 equivale a: ", porcentajeNota3, " es " , nota3)
print("Su nota 4 equivale a: ", porcentajeNota4, " es " , nota4)
print("Su nota 5 equivale a: ", porcentajeNota5, " es " , nota5)

print("Su calificación definitiva es: ", notaFinal)
