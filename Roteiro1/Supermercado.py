dia=input()
preco=float(input())
opcao=input()
nome=input()
if (dia == "seg") and (opcao == "ouro") or (dia == "ter") and (opcao == "ouro") or (dia == "qua") and (opcao == "ouro"):
    a=(preco/2)
    print("O preco do produto",nome,"no dia",dia,"eh","%.2f"%a)
elif (dia == "qui") and (preco >= 10) and (preco <= 100) or (dia == "sex") and (preco >= 10) and (preco <= 100):
    b=(preco/3)
    print("O preco do produto",nome,"no dia",dia,"eh","%.2f"%b)
elif (dia == "sab") and (opcao == "prata"):
    c=(preco*3)
    print("O preco do produto",nome,"no dia",dia,"eh","%.2f"%c)
else:
    d=(preco*2)
    print("O preco do produto",nome,"no dia",dia,"eh","%.2f"%d)