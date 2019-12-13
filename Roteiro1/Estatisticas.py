time=input()
if (time == "GSW") or (time == "HOU") or (time == "CLE") or (time == "BOS"):
    nome=input()
    tentados=int(input())
    convertidos=int(input())
    tentados2=int(input())
    convertidos2=int(input())
    total=(2*convertidos)+(3*convertidos2)
    percentual=((convertidos*100)/tentados)
    percentual2=((convertidos2*100)/tentados2)
    if (total > 30) or (percentual > 50 and tentados > 10) or (percentual2 > 40 and tentados2 > 7):
        print("O time",time,"estah jogando, e",nome,"estah indo bem.")
    else:
        print("O time",time,"estah jogando, mas",nome,"nao estah indo bem.")
else:
    print("Nenhum time de interesse jogando.")