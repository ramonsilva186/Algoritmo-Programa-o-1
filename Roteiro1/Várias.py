nota1=int(input())
nota2=int(input())
nota3=int(input())
peso1=int(input())
peso2=int(input())
peso3=int(input())
if (nota1 >= 1) and (nota1 <= 100) and (nota2 >= 1) and (nota2 <= 100) and (nota3 >= 1) and (nota3 <= 100) and (peso1 >= 1) and (peso1 <= 10) and (peso2 >= 1) and (peso2 <= 10) and (peso3 >= 1) and (peso3 <= 10):
    a=(nota1+nota2+nota3)/3
    p=((nota1*peso1)+(nota2*peso2)+(nota3*peso3))/(peso1+peso2+peso3)
    h=3/(1/nota1+1/nota2+1/nota3)
    print("a:","%.1f"%a)
    print("p:","%.1f"%p)
    print("h:","%.1f"%h)