'''
Leia linhas da entrada padrão até que um número negativo seja digitado. Quais os
cinco maiores números. Suponha que sempre se faça mais de cinco
leituras e que os números lidos sejam sempre distintos. Não considere
o número negativo, pois é só um delimitador de fim
'''


listaDeMaiores = [0] * 5
entrada = float(input("Digite um número: "))
while entrada >= 0:
    if entrada > listaDeMaiores[0]:
        listaDeMaiores[0] = entrada
        listaDeMaiores.sort()
    entrada = float(input("Digite um número: "))
print(listaDeMaiores)