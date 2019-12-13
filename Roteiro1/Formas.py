forma=input()
if (forma == "Q"):
    ladoq=float(input())
    areaq=(ladoq**2)
    peri=(ladoq*4)
    print("%.2f"%areaq)
    print("%.2f"%peri)
elif (forma == "R"):
    largura=float(input())
    altura=float(input())
    arear=(largura*altura)
    perir=(2*altura)+(2*largura)
    print("%.2f"%arear)
    print("%.2f"%perir)
elif (forma == "C"):
    raio=float(input())
    areac=(3.14*(raio**2))
    comp=(2*3.14*raio)
    print("%.2f"%areac)
    print("%.2f"%comp)
else:
    print("Nenhuma figura selecionada")