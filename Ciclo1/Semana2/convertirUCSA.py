print("Programa para convertir UCSA")

uo = int(input("Unidad origen: 1.Barril 2.Galon 3.Cuarto 4.Pinta 5.Onza? "))
co = float(input("Cantidad? "))
ud = int(input("Unidad origen: 1.Barril 2.Galon 3.Cuarto 4.Pinta 5.Onza? "))


#validaciones
if uo in range(1, 6) and ud in range(1, 6) and \
    co >= 0:

    #Proceso
    #Unidad origen, convertir a onzas
    if uo == 1:
        #Barril
        cd = co * 2688
        nuo = "Barril(es)"
    elif uo == 2:
        #Galon
        cd = co * 64
        nuo = "Galon(es)"
    elif uo == 3:
        #Cuarto
        cd = co * 16
        nuo = "Cuarto(es)"
    elif uo == 4:
        #Pinta
        cd = co * 8
        nuo = "Pinta(s)"
    else:
        #Onza
        cd = co
        nuo = "Onza(s)"

     #Unidad destino, convertir de onzas a otra unidad
    if ud == 1:
        # Barril
        cd = cd / 2688
        nud = "Barril(es)"
    elif ud == 2:
        # Galon
        cd = cd / 64
        nud = "Galon(es)"
    elif ud == 3:
        # Cuarto
        cd = cd / 16
        nud = "Cuarto(s)"
    elif ud == 4:
        # Pinta
        cd = cd / 8
        nud = "Pinta(s)"

    print(co, " ", nuo, " son ", cd, " ", nud)
else:
    print("Los datos no son validos")