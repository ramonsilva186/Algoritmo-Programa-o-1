psnr=int(input())
enq=input()
expo=input()
if (80 <= psnr <= 90):
    if (enq == "bom" or enq == "excelente") and (expo == "bem exposta"):
        print("para imprimir")

    elif (expo == "subexposta" or expo == "superexposta"):
        print("boa")

    else:
        print("marromeno")

elif (50 <= psnr <= 80):
    if (enq == "excelente") and (expo == "bem exposta"):
        print("boa")

    else:
        print("marromeno")

elif (psnr < 50):
    if (enq == "excelente") and (expo == "bem exposta"):
        print("marromeno")

    else:
        print("lixo")