print("El programa muestra el numero romano, según el numero arábigo ingresado")

valorArabigo = int(input("Ingresar número árabigo: "))

if valorArabigo > 0 and valorArabigo < 4000:

    valorArabigoInicial = valorArabigo
    valorRomano = ""

    while valorArabigo > 0:
        if valorArabigo >= 1000:
            valorArabigo -= 1000
            valorRomano += "M"
        elif valorArabigo >= 900:
            valorArabigo -= 900
            valorRomano += "CM"
        elif valorArabigo >= 500:
            valorArabigo -= 500
            valorRomano += "D"
        elif valorArabigo >= 400:
            valorArabigo -= 400
            valorRomano += "CD"
        elif valorArabigo >= 100:
            valorArabigo -= 100
            valorRomano += "C"
        elif valorArabigo >= 90:
            valorArabigo -= 90
            valorRomano += "XC"
        elif valorArabigo >= 50:
            valorArabigo -= 50
            valorRomano += "L"
        elif valorArabigo >= 40:
            valorArabigo -= 40
            valorRomano += "XL"
        elif valorArabigo >= 10:
            valorArabigo -= 10
            valorRomano += "X"
        elif valorArabigo >= 9:
            valorArabigo -= 9
            valorRomano += "IX"
        elif valorArabigo >= 5:
            valorArabigo -= 5
            valorRomano += "V"
        elif valorArabigo >= 4:
            valorArabigo -= 4
            valorRomano += "IV"
        else:
            valorArabigo -= 1
            valorRomano += "I"

    print("El valor en número arabigo es: ", valorArabigoInicial ," el número romano es: ",valorRomano)

else:
    print("dato no valido")

