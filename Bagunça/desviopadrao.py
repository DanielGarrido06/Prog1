from math import sqrt


qtdNumeros = int(input("Digite a quantidade de números: "))
numeros = [0] * qtdNumeros
for i in range(0, qtdNumeros):
    numeros[i] = float(input("Digite o número: "))
media = sum(numeros) / qtdNumeros
somatorio = 0

for i in range(0, qtdNumeros):
    somatorio += (numeros[i] - media) ** 2
desvioPadrao = sqrt(somatorio / qtdNumeros)


print("Média: ", media)
print("Desvio padrão: ", desvioPadrao)

