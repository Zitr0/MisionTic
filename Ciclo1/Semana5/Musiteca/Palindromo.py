from MisionTic.Ciclo1.Semana5.Musiteca.Pila import Pila

frase = input("Frase a validar?")

frase = frase.replace(" ", "").replace("á", "a").lower()

mitad = int(len(frase)/2)

#Crear la pila para guardar los caracteres hasta la mitad de la frase
p = Pila()

print("Caracteres apilados")
for i in range(0, mitad):
    p.apilar(frase[i])
    print(frase[i])

i = mitad
if len(frase) % 2 == 1:
    i += 1

print("Caracteres desapilados")
esPalindromo = True
while not p.vacia() and esPalindromo:
    caracter = p.desapilar()
    print(caracter, " - ", frase[i])
    if caracter != frase[i]:
        esPalindromo = False
    i += 1

if esPalindromo:
    print("La frase es un palíndromo")
else:
    print("La frase NO es un palíndromo")


