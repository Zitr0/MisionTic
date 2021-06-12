print("El programa muestra el numero romano, según el numero arábigo ingresado")

try:
    valorArabigo = int(input("Ingresar número árabigo: "))

    if valorArabigo > 0 and valorArabigo < 4000:

        romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        valorArabigoInicial = valorArabigo
        valorRomano = ""
        p = 0
        while valorArabigo > 0:
            #Buscar el siguiente valor disponible para el numero romano
            while valorArabigo < valores[p]:
                p += 1

            valorArabigo -= valores[p]
            valorRomano += romanos[p]

        print("El valor en número arabigo es: ", valorArabigoInicial ," el número romano es: ",valorRomano)

    else:
        print("dato no valido")
except Exception as e:
    print("Error en la entrada de datos\n [", e, "]")