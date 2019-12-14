import math
cont=0
dia=0
soma=0
while cont < 7:
    n=int(input())

    if n >= 100:
        dia += 1

    cont += 1
    soma += n
    media=(soma/7)


print(dia)
print(math.floor(media))