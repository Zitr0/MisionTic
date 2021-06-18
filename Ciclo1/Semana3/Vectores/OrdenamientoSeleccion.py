def buscarDato(d, V):
    i = 1
    while i <= V[0] and V[i] != d:
           i = i + 1
    if i <= V[0]:
           return i
        return -1