def busbin(self, d):
    inicio = 1
    fin = self.V[0]
    while inicio <= fin:
          mitad = (inicio + fin) // 2
          if self.V[mitad] == d:
               return mitad
          if d < self.V[mitad]:
              fin = mitad – 1
         else:
             inicio = mitad + 1
return –1

def buscarDato(d, V):
    i = 1
    while i <= V[0] and V[i] != d:
           i = i + 1
    if i <= V[0]:
           return i
        return -1

def ordenaAscen(V):
    for i in range(1, V[0]):
        for j in range(1, V[0] – I + 1):
             if V[j] > V[j + 1]:
                    intercambiar(V, j, j + 1)


def ordenaAscen(V)
    for i in range(1, V[0]):
        k = i
        for j in range(i + 1, V[0] + 1):
            if V[j] < V[k]:
                k = j
        intercambiar(V, i, k)

def insercion(V):
    for i in range(2, V[0]+1):
        d = V[i]
        j = i -1
        while j > 0  and  V[j] > d:
            V[j+1] = V[j]
            j = j -1
        V[j+1] = d