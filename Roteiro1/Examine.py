temp=float(input())
sec=input()
if (temp >= 37) and (temp <= 41) and (sec == "S"):
    print("Exames Especiais")
elif (temp >= 37) and (sec == "N"):
    print("Exames Basicos")
elif (temp < 37) and (sec == "N"):
    print("Liberado")
elif (temp < 37) and (sec == "S"):
    print("Exames Basicos")
else:
    print("Erro")