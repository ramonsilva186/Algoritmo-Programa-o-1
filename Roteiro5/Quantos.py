def digito(a):
    cont = 0
    l = ["0","1","2","3","4","5","6","7","8","9"]
    for i in range(len(a)):
        if a[i] in l:
            cont += 1
    return cont

x = input()
print(digito(x))
