'''
Leia na primeira linha da entrada padrão, o teclado, um número inteiro positivo, definindo
a quantidade de números a serem lidos nas linhas subsequentes da
entrada padrão. Identifique e escreva qual o número mais frequente.
Caso haja empate escreva o número mais frequente que foi lido primeiro
'''

n = int(input("Quantos números deseja inserir? "))
numeros = [0] * n
for i in range(n):
    numero = float(input("Digite um número: "))
    numeros[i] = numero

max_count = 0
moda = numeros[0]

for i in range(n):
    count = 0
    for j in range(n):
        if numeros[j] == numeros[i]:
            count += 1

    if count > max_count:
        max_count = count
        moda = numeros[i]

print(f"A moda dos números inseridos é: {moda}")
