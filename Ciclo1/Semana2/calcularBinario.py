print("Programa para convertir de números decimales a binarios")

numeroDecimal = int(input("Ingresar número decimal: "))

if numeroDecimal >= 0:

    numeroBinario = ""
    while numeroDecimal > 1:
        # obtener residuo con el operador %
        digitoBinario = numeroDecimal % 2
        numeroBinario = str(digitoBinario) + numeroBinario

        # Division entera con //  para el cociente
        numeroDecimal = numeroDecimal // 2

    numeroBinario = str(numeroDecimal) + numeroBinario

    print("El numero binario es", numeroBinario)

else:
    print("Digite un numero entero mayor o igual a cero")