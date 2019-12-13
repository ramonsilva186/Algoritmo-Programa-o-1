tipo=input()
if (tipo == "a") or (tipo == "p") or (tipo == "h"):
    nota1=int(input())
    nota2=int(input())
    nota3=int(input())
    if (tipo == "p"):
        p1=int(input())
        p2=int(input())
        p3=int(input())
        p=((nota1*p1)+(nota2*p2)+(nota3*p3))/(p1+p2+p3)
        if (p >= 70) and (p <= 100):
            print("%.2f"%p)
            print("Aprovado")
        elif (p >= 0) and (p <= 40):
            print("%.2f"%p)
            print("Reprovado")
        elif (p >= 40) and (p <= 70):
            print("%.2f"%p)
            print("Final")
    elif (tipo == "a"):
        a=(nota1+nota2+nota3)/3
        if (a >= 70) and (a <= 100):
            print("%.2f"%a)
            print("Aprovado")
        elif (a >= 0) and (a <= 40):
            print("%.2f"%a)
            print("Reprovado")
        elif (a >= 40) and (a <= 70):
            print("%.2f"%a)
            print("Final")
    elif (tipo == "h"):
        h=3/(1/nota1+1/nota2+1/nota3)
        if (h >= 70) and (h <= 100):
            print("%.2f"%h)
            print("Aprovado")
        elif (h >= 0) and (h <= 40):
            print("%.2f"%h)
            print("Reprovado")
        elif (h >= 40) and (h <= 70):
            print("%.2f"%h)
            print("Final")
else:
    print("Escolha um tipo de media valida.")



