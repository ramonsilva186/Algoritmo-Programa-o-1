media=0
homi=0
mule=0
salario_homi=0
sal_total=0
media1=0
maior_salario = 0

for i in range(0,10):
    salario=float(input())
    sal_total += salario
    sexo=input()

    if (salario > maior_salario):
        maior_salario = salario
        sexo_m = sexo

    media=(sal_total/10)

    if sexo == "f":
        mule +=1

    elif sexo == "m":
        homi +=1
        salario_homi += salario
        media1=(salario_homi/homi)



print(homi)
print(mule)
print("%.1f"%media)
print(sexo_m)
print("%.1f"%media1)



