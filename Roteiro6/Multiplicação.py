matriz = []

for x in range(4):
    lista=[]
    for y in range(4):
        lista.append(0)
    matriz.append(lista)

while True:
    k = int(input())

    if k == 0:
        break

    for i in range(4):
        for j in range(4):
            valores = int(input())
            matriz[j][i]= valores

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i] == matriz[j]:
                matriz[i][j] *= k

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()