candidato1 = 0
candidato2 = 0
candidato3 = 0
nulo = 0
branco = 0
eleitores = 0
voto = int(input("Digite o número do candidato: "))


while voto >= 0 and voto <= 4:
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
    eleitores += 1
    voto = int(input("Digite o número do candidato: "))

if candidato2 > candidato1:
    vencedor = "Candidato 2"
if candidato3 > candidato2:
    vencedor = "Candidato 3"
if candidato1 > candidato3:
    vencedor = "Candidato 1"

print("Vencedor:", vencedor)
print("Eleitores:", eleitores)
print("Nulos:", nulo)
print("Brancos:", branco)

