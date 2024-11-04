'''
Leia na primeira linha da entrada
padrão, isto é: o teclado, um número inteiro positivo maior que zero,
definindo a quantidade de pares de números, x e y, a serem lidos nas
linhas subsequentes da entrada padrão. Cada par representando as
coordenadas de um ponto. Calcule e escreva o centro geométrico dos
pontos lidos. Em seguida identifique e escreva qual o ponto mais
distante do centro geométrico calculado.
'''


#Passo "zero": importar a função sqrt do módulo math
#Essa função é utilizada para calcular a raiz quadrada de um número
#Ela será utilizada para calcular a distância entre os pontos e o centro geométrico
from math import sqrt


#Primeiro, pedimos ao usuário que digite o número de pares de números que ele deseja inserir
#Depois, criamos uma lista vazia para armazenar os pares de números, cada par representando as coordenadas de um ponto no plano cartesiano
#Em seguida, pedimos ao usuário que insira os pares de números e os armazenamos na lista
#A entrada é separada em duas partes, utilizando o método 'split', que separa a string em duas partes, utilizando um espaço como delimitador
#Isso é feito para que possamos armazenar os números em uma lista de listas, onde cada sublista contém dois números
#O método 'split' retorna uma lista de strings, então convertemos os números para o tipo 'float', para possibilitar operações matemáticas
#Exemplo: se o usuário digitar 2.0 1.0, a entrada será separada em duas strings: ['2.0', '1.0']
#Depois, convertemos as strings para float: [2.0, 1.0]
#Ao fim desse processo, teremos uma lista de listas, onde cada sublista contém dois números, representando as coordenadas de um ponto
numero_de_pontos = int(input("Digite o número de pares: "))
lista_de_pontos = [0] * numero_de_pontos
for i in range(numero_de_pontos):
    par = input("Digite um par de números: ")
    lista_de_pontos[i] = par.split(" ")
    lista_de_pontos[i][0] = float(lista_de_pontos[i][0])
    lista_de_pontos[i][1] = float(lista_de_pontos[i][1])


#Agora, calculamos o centro geométrico dos pontos
#Para isso, somamos as coordenadas de todos os pontos e dividimos pela quantidade de pontos
#Cada coordenada é somada separadamente, para que possamos calcular a média de cada coordenada
#O centro geométrico é o ponto cujas coordenadas x,y são a média de todas as coordenadas x,y dos pontos
#Ao fim desse processo, teremos as coordenadas do centro geométrico armazenadas na lista centro_geometrico
centro_geometrico = [0.0, 0.0]
for i in range(numero_de_pontos):
    centro_geometrico[0] += lista_de_pontos[i][0]
    centro_geometrico[1] += lista_de_pontos[i][1]
centro_geometrico[0] /= numero_de_pontos
centro_geometrico[1] /= numero_de_pontos


#Por fim, identificamos o ponto mais distante do centro geométrico
#Para isso, calculamos a distância de cada ponto ao centro geométrico e verificamos qual é a maior
#A distância entre dois pontos (x1, y1) e (x2, y2) é dada pela fórmula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
#Como a distância entre dois pontos é sempre positiva, podemos inicializar a maior_distancia com um valor negativo
#Para garantir que qualquer distância calculada no primeiro ponto será maior que esse valor e, portanto, atualizará a maior_distância corretamente
ponto_mais_distante = [0,0]
maior_distancia = -1
for ponto in lista_de_pontos:
    dist = sqrt((ponto[0] - centro_geometrico[0]) ** 2 + (ponto[1] - centro_geometrico[1]) ** 2)
    if dist > maior_distancia:
        maior_distancia = dist
        ponto_mais_distante = ponto


#Por fim, imprimimos o centro geométrico e o ponto mais distante
#Utilizamos o comando ':.2f' para formatar as strings exibidas como saída, limitando o número de casas decimais a 2
print(f"Centro Geométrico: [{centro_geometrico[0]:.2f}, {centro_geometrico[1]:.2f}]")
print(f"Ponto mais distante: [{ponto_mais_distante[0]:.2f}, {ponto_mais_distante[1]:.2f}] com distância {maior_distancia:.2f}")