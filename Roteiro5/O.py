def maior(a):
    l = []
    x = 0

    for i in range(len(n)):
        l.append(int(n[i]))
        l.sort()
        x = l[-1]
    return x

n = input().split()
print(maior(n), "eh o maior")
