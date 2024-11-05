'''
Questão 3 – Faça um programa que leia inicialmente um número inteiro modelando a quantidade
 de números de ponto flutuante que se sucederão nas linhas de leitura a seguir. Calcule e
 escreva a média dos números de ponto flutuante lidos. Para cada número de ponto
 flutuante lido escreva se está acima, está abaixo ou é igual à média calculada.
'''

# 1. Leitura do número de números de ponto flutuante:
quantidade = int(input("Digite a quantidade de números de ponto flutuante: "))

# 2. Inicialização de variáveis:
soma = 0
listaDeNumeros = [0] * quantidade

# 3. Leitura dos números de ponto flutuante:
for i in range(quantidade):
    listaDeNumeros[i] = float(input("Digite um número de ponto flutuante: "))
    soma += listaDeNumeros[i]

# 4. Cálculo e impressão da média:
media = soma / quantidade
print(f"Média Calculada dos Números: {media}")

# 5. Comparação dos números com a média:
for i in range(quantidade):
    if listaDeNumeros[i] > media:
        print(f"{listaDeNumeros[i]} está acima da média")
    elif listaDeNumeros[i] < media:
        print(f"{listaDeNumeros[i]} está abaixo da média")
    else:
        print(f"{listaDeNumeros[i]} é igual à média")

# 5b. Comparação dos números com a média (Sintaxe alternativa):
# Esse trecho de código faz a mesma coisa que o trecho de código acima, mas escrito de uma forma diferente
# Então, ele não é necessário para o funcionamento do programa, mas é uma alternativa de implementação
# E está aqui somente para exemplificar que existem várias formas de escrever um mesmo código, por isso está comentado
'''
for numero in listaDeNumeros:
    if numero > media:
        print(f"{numero} está acima da média")
    elif numero < media:
        print(f"{numero} está abaixo da média")
    else:
        print(f"{numero} é igual à média")
'''
