nota1=int(input())
nota2=int(input())
nota3=int(input())
media=((nota1+nota2+nota3)/3)
if (media >= 40) and (media <= 70):
    print("A media do aluno foi","%.2f"%media,"e ele foi FINAL")
elif (media >= 0) and (media <= 40):
    print("A media do aluno foi","%.2f"%media,"e ele foi REPROVADO")
elif (media >= 70) and (media <= 100):
    print("A media do aluno foi","%.2f"%media,"e ele foi APROVADO")
else:
    print("Media invalida")