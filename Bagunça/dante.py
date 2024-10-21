nulo = 0
candidato1 = 0
candidato2 = 0
candidato3 = 0
branco = 0

while True:
    voto = int(input("Digite seu voto: "))
    if voto == 0:
        nulo += 1
    elif voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 4:
        branco += 1
    else:
        print("Voto inválido\n")
        break

print("Votos nulos: ", nulo)
print("Votos candidato1: ", candidato1)
print("Votos candidato2: ", candidato2)
print("Votos candidato3: ", candidato3)
print("Votos brancos: ", branco)
if max(candidato1, candidato2, candidato3) == candidato1:
    print("Candidato Vencedor: Candidato 1")
elif max(candidato1, candidato2, candidato3) == candidato2:
    print("Candidato Vencedor: Candidato 2")
else:
    print("Candidato Vencedor: Candidato 3")
print("Total de votos: ", nulo + candidato1 + candidato2 + candidato3 + branco)

