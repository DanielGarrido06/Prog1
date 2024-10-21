"""
Este script solicita ao usuário que insira números repetidamente até que um número negativo seja inserido.
Ele realiza as seguintes operações:
1. Inicializa as variáveis 'soma_de_positivos', 'numero_de_positivos' com zero.
2. Solicita ao usuário que insira um número.
3. Inicializa as variáveis 'maiornumero' e 'menornumero' com o número inserido.
4. Enquanto o número inserido for positivo:
    - Adiciona o número à variável 'soma_de_positivos'.
    - Incrementa o contador 'numero_de_positivos'.
    - Atualiza 'maiornumero' se o número inserido for maior que o valor atual de 'maiornumero'.
    - Atualiza 'menornumero' se o número inserido for menor que o valor atual de 'menornumero'.
    - Solicita ao usuário que insira outro número.
5. Após a inserção de um número negativo, o loop é encerrado e o script imprime:
    - O menor número positivo inserido.
    - O maior número positivo inserido.
    - A média dos números positivos inseridos.
"""
soma_de_positivos = 0
numero_de_positivos = 0
num = float(input("Digite um número (negativo para parar): "))
maiornumero = num
menornumero = num
while num >= 0:
    soma_de_positivos += num
    numero_de_positivos += 1
    if num > maiornumero:
        maiornumero = num
    if num < menornumero:
        menornumero = num
    num = float(input("Digite um número (negativo para parar): "))    

print(f"Menor número positivo: {menornumero}")
print(f"Maior número positivo: {maiornumero}")
print(f"Média dos números positivos: {soma_de_positivos / numero_de_positivos}")