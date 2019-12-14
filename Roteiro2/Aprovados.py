cont=0
pt=0
mat=0
red=0
while True:
    acerto_pt=int(input())
    pt = acerto_pt

    if (acerto_pt < 0):
        break

    acerto_mat=int(input())
    mat = acerto_mat

    redacao=float(input())
    red = redacao

    if (pt >= 0.8*50) and (mat >= 0.6*35) and (red >= 7):
        cont += 1

print(cont)

