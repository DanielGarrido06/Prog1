numCadidatos = int(input("Digite o número de candidatos: "))
listaCandidatos = [0] * (numCadidatos + 2)
voto = int(input("Digite o número do candidato: "))
eleitores = 0

while voto >= 0 and voto <= numCadidatos + 1:
    listaCandidatos[voto] += 1
    eleitores += 1
    voto = int(input("Digite o número do candidato: "))

vencedor = 1
for i in range(2, numCadidatos + 1):
    if listaCandidatos[i] > listaCandidatos[vencedor]:
        vencedor = i

print("Vencedor:", vencedor)
print("Eleitores:", eleitores)
print("Nulos:", listaCandidatos[0])
print("Brancos:", listaCandidatos[numCadidatos + 1])