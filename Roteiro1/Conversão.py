unid=str(input())
temp=float(input())
if unid == "C" and (temp >= -273.0):
    f=((9*temp)/5)+32
    k=temp+273.15
    print("%.2f"%f+ " F")
    print("%.2f"%k+ " K")
elif unid == "F" and (temp >= -459.67):
   c=((temp-32)*5)/9
   k1=((temp+459.67)*5)/9
   print("%.2f"%c+ " C")
   print("%.2f"%k1+ " K")
elif unid == "K" and (temp >= 0.0):
    f1=(temp*1.8)-459.67
    c1=temp-273.15
    print("%.2f"%c1+ " C")
    print("%.2f"%f1+ " F")

else:
    print("Valor de temperatura abaixo do minimo")