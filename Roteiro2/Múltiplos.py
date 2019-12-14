n=int(input())
a=int(input())
b=int(input())
if a < n > b:
    print("INEXISTENTE")

for i in range(a,b+1):
    if (i % n) == 0:
        print(i)
