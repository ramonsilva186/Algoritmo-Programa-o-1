n=int(input())
contador=0
if (1 <= n < 1000):
    while (contador < n):
        contador += 1
        q=contador**2
        c=contador**3
        print(contador, q, c)