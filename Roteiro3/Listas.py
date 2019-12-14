n = int(input())

if n != 0:

    lista_notas = []
    soma = 0

    for i in range(1, n+1):
        nota = float(input())
        soma += nota
        lista_notas.append(nota)

        print("Nota {}: {}".format(i,nota))

    media=(soma/n)



    print("Media:", "%.2f"%media)

else:
    print("Numero de notas invalido.")