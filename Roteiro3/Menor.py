lista = []

n = int(input())

if 1 > n > 1000:
    print("Erro")

else:
    valor = input().split(" ")

for i in valor:
    lista.append(int(i))

menor_numero = min(lista)
a = lista.index(menor_numero)
print("Menor valor:",menor_numero)
print("Posicao:",a)