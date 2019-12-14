t = int(input())
if 1 < t > 4:
    print("Erro")

cont = 0
resp = input().split()

for i in resp:
    valor = int(i)
    if valor == t:
        cont += 1


print(cont)
