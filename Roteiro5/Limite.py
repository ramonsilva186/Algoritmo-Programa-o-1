def multa(x):
    a = 0
    if 50 < x <= 55:
        a = 230.00
    elif 55 < x <= 60:
        a = 340.00
    elif x > 60:
        a = (x - 50)*19.28
    return a

n = int(input())
print("%.2f"%multa(n))
