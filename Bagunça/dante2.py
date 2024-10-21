def main():
    # Solicita ao usuário o número de candidatos
    num_candidatos = int(input("Digite o número de candidatos: "))
    
    # Inicializa contadores de votos
    nulo = 0
    branco = 0
    candidatos = [0] * num_candidatos
    
    while True:
        voto = int(input("Digite seu voto: "))
        if voto == 0:
            nulo += 1
        elif voto == num_candidatos + 1:
            branco += 1
        elif 1 <= voto <= num_candidatos:
            candidatos[voto - 1] += 1
        else:
            print("Voto inválido\n")
            break
    
    # Exibe os resultados dos votos
    print("Votos nulos: ", nulo)
    for i in range(num_candidatos):
        print(f"Votos candidato{i + 1}: ", candidatos[i])
    print("Votos brancos: ", branco)
    
    # Determina e exibe o candidato vencedor
    vencedor = candidatos.index(max(candidatos)) + 1
    print(f"Candidato Vencedor: Candidato {vencedor}")
    print("Total de votos: ", nulo + branco + sum(candidatos))

if __name__ == "__main__":
    main()