lista_1 = []
lista_2 = []
lista_3 = list()

n = int(input())

for i in range(0, n):
    valor_1 = int(input())
    lista_1.append(valor_1)

for i in range(0, n):
    valor_1 = int(input())
    lista_2.append(valor_1)

for i in range(0, n):
    lista_3.append(lista_1[i])
    lista_3.append(lista_2[i])

for i in range(len(lista_3)):
    print(lista_3[i])