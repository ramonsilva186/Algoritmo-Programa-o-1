def mes(a):
    l = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    x = l[a-1]
    return x

n = int(input())

if n < 1 or n > 12:
    print("invalido")

else:
    print(mes(n))