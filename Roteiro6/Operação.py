debitos = []
creditos = []
soma_creditos = 0
soma_debidos = 0

while True:
    n = input().split()

    if n[0] == "-1":
        break

    if n[0] == "1":
        creditos.append(n[1])
    elif n[0] == "0":
        debitos.append(n[1])

for i in range(len(creditos)):
    creditos[i] = float(creditos[i])
    soma_creditos += creditos[i]

for i in range(len(debitos)):
    debitos[i] = float(debitos[i])
    soma_debidos += debitos[i]

saldo = soma_creditos - soma_debidos

print("Creditos: R$","%.2f"%soma_creditos)
print("Debitos: R$","%.2f"%soma_debidos)
print("Saldo: R$","%.2f"%saldo)