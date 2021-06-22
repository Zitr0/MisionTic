V = [8, 3, 1, 6, 2, 7, 4, 9, 5]
for i in range(8, 1, -1):
        V[i] = V[(i-1)%8]
for i in range(1, 9):
        print(V[i], sep=",", end=" ")