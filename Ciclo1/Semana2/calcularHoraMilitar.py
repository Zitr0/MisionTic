print("Programa para convertir hora regular en hora militar")

hora = int(input("Hora? "))
minuto = int(input("Minutos? "))
jornada = int(input("Jornada:  1.AM  2.PM "))

# Validaciones

if hora in range(1, 13) and \
        minuto in range(0, 60) and \
        jornada in range(1, 13):
    # Proceso
    horaMilitar = hora
    if jornada == 2:
        if hora < 12:
            horaMilitar += 12
    else:
        if horaMilitar == 12:
            horaMilitar = 0

    print("La hora militar es: ", "{0:02d}{1:02d}".format(horaMilitar, minuto))
else:
    print("Los datos no son válidos")

