acima = 0
abaixo = 0
notas = []
soma = 0

n = int(input())

for i in range(1, n+1):
    nota = float(input())
    notas.append(nota)
    soma += nota

media = soma/n

for i in notas:

    if i > media+media*0.1:
        acima += 1

    elif i < media-media*0.1:
        abaixo += 1

print("%.2f"%media)
print(acima)
print(abaixo)