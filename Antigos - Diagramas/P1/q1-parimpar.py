'''
 Questão 1 – Faça um programa que leia cinco números inteiros e para cada número lido escreva
 se ele é par ou é ímpar. Ao final, escreva a quantidade de pares e a quantidade de
 ímpares.
'''

# 1. Inicialização de Contadores:
# Dois contadores são inicializados para contar quantos números pares e ímpares o usuário digitar.
contPares = 0
contImpares = 0

# 2. Loop de 5 iterações:
# O loop for é utilizado para iterar 5 vezes, pedindo um número ao usuário a cada iteração.
for i in range(5):
    num = int(input("Digite um número: "))
    # O operador % retorna o resto da divisão entre dois números. Se o resto da divisão de um número por 2 for 0, então ele é par.
    # Se o número for par, imprime esse resultado, e incrementa o contador de pares.
    if num % 2 == 0:
        print(f"{num} é par")
        contPares += 1
    # Se o número não for par, então ele é ímpar. Imprime esse resultado, e incrementa o contador de ímpares.
    else:
        print(f"{num} é ímpar")
        contImpares += 1

# 3. Impressão dos resultados:
# Após o loop, imprime a quantidade de números pares e ímpares que o usuário digitou.
print(f"Quantidade de pares: {contPares}")
print(f"Quantidade de ímpares: {contImpares}")