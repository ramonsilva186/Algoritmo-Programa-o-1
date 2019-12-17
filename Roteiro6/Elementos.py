def diagonal_primaria(matriz):
    diagonal_p = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i] == matriz[j]:
                diagonal_p += matriz[i][j]
    return diagonal_p

def diagonal_secundaria(matriz):
    diagonal_s = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if (i+j) == len(matriz[i])-1:
                diagonal_s += matriz[i][j]
    return diagonal_s

matriz = []
maior = 0
menor = 0

tam_matriz = input().split()

linha = int(tam_matriz[0])
coluna = int(tam_matriz[1])

for i in range(linha):
    matriz.append([])
    for j in range(coluna):
        valores = int(input())
        matriz[i].append(valores)
        if valores > 0:
            maior += 1
        elif valores < 0:
            menor += 1


print("Matriz formada:")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j == len(matriz[i])-1:
            print(matriz[i][j], end = '\n')
        else:
            print(matriz[i][j], end=' ')
    
if linha == coluna:
    print("A diagonal principal e secundaria tem valor(es)",diagonal_primaria(matriz),"e",diagonal_secundaria(matriz),"respectivamente.")
else:
    print("A diagonal principal e secundaria nao pode ser obtida.")

print("A matriz possui",menor,"numero(s) menor(es) que zero.")
print("A matriz possui",maior,"numero(s) maior(es) que zero.")