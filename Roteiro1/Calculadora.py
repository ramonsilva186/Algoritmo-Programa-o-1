carne=input()
if (carne == "C") or (carne == "BF") or (carne == "BS"):
    alho=input()
    bebidaa=input()
    bebidac=input()
    quantidadec=int(input())
    quantidadea=int(input())
    if (carne == "C") and (alho == "S") and (bebidaa == "S") and (bebidac == "S"):
        total=(6.4*quantidadea)+(1.8*quantidadea)+(1.5*quantidadea)+(6.4*quantidadec)+(8*2*quantidadea)+(6*0.5*quantidadec)
        print("R$:","%.2f"%total)

    elif (carne == "BF") and (alho == "N") and (bebidaa == "S") and (bebidac == "S"):
        total1=((8*quantidadea)+(2.7*quantidadea)+(6.4*quantidadec)+(8*2*quantidadea)+(6*0.5*quantidadec))*0.98
        print("R$:","%.2f"%total1)

    elif (carne == "BS") and (alho == "N") and (bebidaa == "S") and (bebidac == "S"):
        total2=((8*quantidadea)+(2.25*quantidadea)+(6.4*quantidadec)+(8*2*quantidadea)+(6*0.5*quantidadec))*0.98
        print("R$:","%.2f"%total2)

    elif (carne == "BF") and (alho == "S") and (bebidaa == "N") and (bebidac == "N"):
        total3=(8*quantidadea)+(2.7*quantidadea)+(6.4*quantidadec)
        print("R$:","%.2f"%total3)

    elif (carne == "C") and (alho == "S") and (bebidaa == "N") and (bebidac == "S"):
        total4=(6.4*quantidadea)+(1.8*quantidadea)+(1.5*quantidadea)+(6.4*quantidadec)+(6*0.5*quantidadec)
        print("R$:","%.2f"%total4)

    elif (carne == "C") and (alho == "N") and (bebidaa == "N") and (bebidac == "S"):
        total5=((6.4*quantidadea)+(1.8*quantidadea)+(1.5*quantidadea)+(6.4*quantidadec)+(6*0.5*quantidadec))*0.98
        print("R$:","%.2f"%total5)
    
    elif (carne == "BS") and (alho == "S") and (bebidaa == "S") and (bebidac == "S"):
        total6=(8*quantidadea)+(2.25*quantidadea)+(6.4*quantidadec)+(8*2*quantidadea)+(6*0.5*quantidadec)
        print("R$:","%.2f"%total6)

else:
    print("Op��o inv�lida.")