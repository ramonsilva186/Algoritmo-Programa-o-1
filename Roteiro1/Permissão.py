idade=int(input())
tipo=input()
if (idade >= 21) and (tipo == "azar"):
    print("Pode entrar!")
elif (idade >= 0) and (idade >= 21) and (tipo == "azar"):
    print("Volte daqui h� alguns anos.")
elif (idade >= 14) and (tipo == "mmorpg"):
    print("Pode entrar!")
elif (idade < 14) and (idade >= 0) and (tipo == "mmorpg"):
    print("Volte daqui h� alguns anos.")
elif (idade >= 10) and (tipo == "moba"):
    print("Pode entrar!")
elif (idade < 10) and (idade >= 0) and (tipo == "moba"):
    print("Volte daqui h� alguns anos.")
elif (idade > 0) and (tipo == "casual"):
    print("Pode entrar!")
elif (idade < 0) and (tipo == "casual"):
    print("Idade invalida.")
elif (idade < 0) and (tipo == "azar"):
    print("Idade invalida.")
elif (idade < 0) and (tipo == "mmorpg"):
    print("Idade invalida.")
elif (idade < 0) and (tipo == "moba"):
    print("Idade invalida.")
elif (idade < 0) and (tipo == "casual"):
    print("Idade invalida.")
elif (idade < 0) and (tipo != "azar") or (idade < 0) and (tipo != "mmorpg") or (idade < 0) and (tipo != "moba") or (idade < 0) and (tipo != "casual"):
    print("Idade invalida.")
elif (tipo != "azar") or (tipo != "mmorpg") or (tipo != "moba") or (tipo != "casual"):
    print("Jogo invalido.")





