def volume(r1):
    v = ((4*3.1416)*(r1**3)/3)
    return (v)

for i in range(0,3):
    r = float(input())
    a = volume(r)
    print("{:.2f}".format(a))