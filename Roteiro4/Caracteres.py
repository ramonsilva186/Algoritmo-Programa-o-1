lista = []
while True:
    n = int(input())
    if n == 0:
        break
    a = input()
    if len(a) > n:
        print("Erro")
        break
    lista.append(a)

for i in lista:
    print(i[::-1])