lista_1 = []
lista_2 = []
lista_3 = []
n1 = int(input())

if n1 == 0:
    print("Erro - A lista deve ter pelo menos 1 elemento.")

else:

    for i in range(1, n1+1):

        valor_1 = int(input())
        lista_1.append(valor_1)

    n2 = int(input())

    if n2 == 0:
        print("Erro - A lista deve ter pelo menos 1 elemento.")

    else:
        for i in range(1, n2+1):

            valor_2 = int(input())
            lista_2.append(valor_2)

        lista_3 = lista_1 + lista_2
        print(' '.join(map(str,lista_3)))