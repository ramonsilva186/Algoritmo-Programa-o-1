soma=0
cont=0
while True:
    n=int(input())
    if n == 0:
        break
    soma += n
    cont += 1
media=(soma/cont)
if (media < 110):
    print("Glicose Normal")
elif (media >= 200):
    print("Glicose Muito Alta")
else:
    print("Glicose Alterada")
