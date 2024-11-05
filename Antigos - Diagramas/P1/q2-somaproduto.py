'''
 Questão 2 – Faça um programa que leia números até que um número negativo seja digitado,
 sendo que o número negativo não deve ser considerado nas contas.  Escreva a soma de
 todos os números lidos. Em seguida, escreva o produto de todos os números lidos. Ao
 final, escreva quantos números não negativos foram lidos.
'''

# 1. Inicialização de variáveis:
# Inicializa-se um contador de números, um acumulador para a soma dos números, e um acumulador para o produto dos números.
# O contador de números e a soma são inicializados com 0, porque serão usados para contablizar somas, e 0 é o elemento neutro da adição.
# O produto é inicializado com 1, porque será usado para contablizar multiplicações, e 1 é o elemento neutro da multiplicação.
contador_de_numeros = 0
soma = 0
produto = 1

# 2. O usuário digita um número, que é lido e armazenado na variável entrada.
entrada = float(input("Digite um número: "))

# 3. Loop de leitura de números:
# O loop while é utilizado para ler números até que um número negativo seja digitado.
# A cada iteração, o número digitado é somado à variável soma, multiplicado à variável produto, e o contador de números é incrementado.
# Se o número digitado for negativo, o loop é encerrado.
while entrada >= 0:
    contador_de_numeros += 1
    soma += entrada
    produto *= entrada
    entrada = float(input("Digite um número: "))

# 4. Impressão dos resultados:
# Após o loop, imprime a soma, o produto e a quantidade de números não negativos que o usuário digitou.
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Quantidade de números não negativos: {contador_de_numeros}")