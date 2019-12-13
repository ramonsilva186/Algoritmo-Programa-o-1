nota1=int(input())
nota2=int(input())
nota3=int(input())
if (nota1 >= nota2) and (nota1 >= nota3) and (nota2 >= nota3):
    print(nota3)
    print(nota2)
    print(nota1)
elif (nota2 >= nota1) and (nota2 >= nota3) and (nota1 >= nota3):
    print(nota3)
    print(nota1)
    print(nota2)
elif (nota3 >= nota2) and (nota3 <= nota1) and (nota2 <= nota1):
    print(nota2)
    print(nota3)
    print(nota1)
elif (nota1 <= nota2) and (nota1 <= nota3) and (nota2 <= nota3):
    print(nota1)
    print(nota2)
    print(nota3)
elif (nota2 <= nota1) and (nota2 <= nota3) and (nota1 <= nota3):
    print(nota2)
    print(nota1)
    print(nota3)
elif (nota1 <= nota3) and (nota1 <= nota2) and (nota3 <= nota2):
    print(nota1)
    print(nota3)
    print(nota2)

    