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
