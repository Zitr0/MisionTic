import funcionesDeVectores as fv


tamagno = 30

vec1 = [0] * (tamagno + 1)

fv.construyeVector(vec1, 16, 99)

fv.imprimeVector(vec1, "vector vec1:\t")

fv.agregarDato(69, vec1, tamagno)

fv.imprimeVector(vec1, "vector vec1 después de agregar dato:\t")

mayor = fv.mayorDato(vec1)

menor = fv.menorDato(vec1)

print("\n el mayor está en la posición", mayor, "y es", vec1[mayor], end = " ")

print("y el menor está en la posición", menor, "y es", vec1[menor])

fv.intercambie(vec1, mayor, menor)

fv.imprimeVector(vec1, "vector vec1 después de intercambiar mayor con menor")



tamagno = 100

vec2 = [0] * (tamagno + 1)

fv.construyeVector(vec2, 26, 999)

fv.imprimeVector(vec2, "vector vec2")

fv.insertarDato(69, 2, vec2, tamagno)

fv.imprimeVector(vec2, "vector vec2 después de insertar dato\t")

fv.ordenaAscen(vec2)

fv.imprimeVector(vec2, "vector vec2 después de ordenarlo")