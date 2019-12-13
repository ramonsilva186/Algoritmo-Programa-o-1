salario=float(input())
horas=int(input())
if (salario >= 1000.00) and (salario <= 10000.00) and (horas >= 0) and (horas <= 50):
    horas1=salario/44
    salario1=(salario+(horas*horas1)*1.1)
    print("%.2f"%salario1)