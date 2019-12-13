crime=input()

if (crime == "roubo") or (crime == "tr�fico"):
    valor=int(input())
    crime1=input()

    if (crime1 == "roubo") or (crime1 == "tr�fico"):
        valor1=int(input())
        if (crime == "roubo" or crime == "tr�fico") and (crime1 == "homic�dio"):
            print("Dela��o concedida.")
        elif (crime == "roubo") and (crime1 == "roubo") and (valor1  > 5* valor):
            print("Dela��o concedida.")
        elif (crime == "roubo") and (crime1 == "tr�fico") and (valor1 > 3* valor):
            print("Dela��o concedida.")
        elif (crime == "tr�fico") and (crime1 == "tr�fico") and (valor1 > 5* valor):
            print("Dela��o concedida.")
        else:
            print("Dela��o rejeitada.")

    elif (crime1 == "homic�dio"):
        print("Dela��o concedida.")

    else:
        print("Crime inv�lido.")

elif (crime == "homic�dio"):
    crime1=input()

    if (crime1 == "roubo") or (crime1 == "tr�fico"):
        valor1=int(input())
        print("Dela��o rejeitada.")
    elif (crime1 == "homic�dio"):
        print("Dela��o concedida.")

else:
    print("Crime inv�lido.")
