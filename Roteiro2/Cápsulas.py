cont=0
p=0
g=0
soma=0
xic=0
while cont < 7:
    quant_caixas=int(input())
    tam_caixa=input()
    cont += 1

    if tam_caixa == "p" or tam_caixa == "P":
        p += quant_caixas

    elif tam_caixa == "g" or tam_caixa == "G":
        g += quant_caixas

    soma=(p*10)+(g*16)
    xic=(soma/7)*2

print(soma)
print("%.f"%xic)

