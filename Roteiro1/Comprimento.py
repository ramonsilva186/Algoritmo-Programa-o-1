raio=float(input())
angulo=float(input())
if (raio >= 1.0) and (raio <= 50.0) and (angulo >= 0.0) and (angulo <= 359.0):
    comp=(angulo*3.14*raio)/180
    area=(angulo*3.14*(raio**2)/360)
    print ("%.2f"%comp)
    print("%.2f"%area)