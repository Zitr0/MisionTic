import random

class vector:

    def __init__(self,n):
        self.n = n
        self.V = [0]*(n+1)
   

    def posiscionesUsadas(self):
        return self.V[0]

    def esVacio(self):
        return self.V[0] == 0

    def esLleno(self):
        return self.V[0] == self.n

    def tamaño(self):
        return self.n

    def imprimeVector(self, mensaje="vector son nombre: \t"):
        print("\n",mensaje, end="")
        for i in range(1, self.V[0]+1):
            print(self.V[i], end =",")
        print()

    def agregarDato(self,d):
        if self.esLleno():
            return
        self.V[0] = self.V[0] + 1
        self.V[self.V[0]] = d

    def intercambiar(self,a,b):
        aux = self.V[a]
            
        self.V[a] = self.V[b]
        self.V[b] = aux

    def sumarDatos(self):
        s = 0
        for i in range(1, self.V[0]+1):
            s = s + self.V[i]
        return s
        