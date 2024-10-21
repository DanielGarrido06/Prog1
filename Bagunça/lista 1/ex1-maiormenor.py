# Lê a quantidade de números
qtdNumeros = int(input("Digite a quantidade de números: "))

# Cria uma lista com a quantidade de números informada
listaDeNumeros = [0] * qtdNumeros

# Inicializa as variáveis maior, menor e soma.
# As variáveis maior e menor são inicializadas com valores de infinito negativo e positivo,
# respectivamente, para garantir que qualquer número inserido pelo usuário será maior que
# maior e menor que menor inicialmente. A variável soma é inicializada com zero para
# acumular a soma dos números inseridos.
maior = float('-inf')
menor = float('inf')
soma = 0

# Lê os números, verifica se são maiores ou menores que os anteriores, e os adiciona à soma total.
# O código entra em um loop que itera qtdNumeros vezes. Em cada iteração, ele solicita ao usuário
# que digite um número, armazena esse número na lista listaDeNumeros e verifica se o número é maior
# que o valor atual de maior ou menor que o valor atual de menor, atualizando essas variáveis
# conforme necessário. Além disso, o número é adicionado à variável soma.
for i in range(qtdNumeros):
    listaDeNumeros[i] = int(input("Digite um número: "))
    if listaDeNumeros[i] > maior:
        maior = listaDeNumeros[i]  
    if listaDeNumeros[i] < menor:
        menor = listaDeNumeros[i]
    soma += listaDeNumeros[i]

# Exibe o menor, o maior e a média dos números
print("Menor:", menor)
print("Maior:", maior)
print("Média:", soma / qtdNumeros)