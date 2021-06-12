print("Obtener el inicio de la semana santa")

#Obtener datos de entrada
ano = int(input("Año a calcular: "))

#Proceso
a = ano % 19
b = ano % 4
c = ano % 7
d = (19 * a + 24) % 30
dias = d + (2*b + 4*c + 6*d + 5) % 7

dia = 15 + dias
mes = "Marzo"

if dia > 31:
    dia = dia - 31
    mes="Abril"

#mostrar los datos de salida
print("La semana santa inicia el ", dia," de ", mes)


