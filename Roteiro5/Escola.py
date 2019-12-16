def situacao(a):
    if nota < 7 and faltas <= 10:
        a = "REPROVADO"
    elif 7 >= nota < 9.5 and faltas <= 10:
        a = "APROVADO"
    elif nota >= 9.5 and faltas <= 10:
        a = "APROVADO COM LOUVOR"
    elif nota > 7 and faltas > 10:
        a = "REPROVADO POR FALTAS"
    return a


nota = float(input())
faltas = int(input())
print(situacao(nota))
