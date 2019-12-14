cont=0
soma=0
while True:
    n=int(input())
    soma += n
    if soma <= 18:
        cont += 1
    elif soma > 18:
        break

print(cont)