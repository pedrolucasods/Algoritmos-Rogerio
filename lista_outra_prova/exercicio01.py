'''
Questão 1: O Contador Regressivo Seletivo

Crie um programa em Python que solicite ao usuário um valor alto (limite superior) e
um valor baixo (limite inferior). O programa deve utilizar um laço for para realizar uma contagem regressiva, 
partindo do valor alto até o baixo, com um passo de -3.

Ao final, exibir:
A média aritmética dos números que fizeram parte da contagem regressiva.
'''

alto = int(input('Informe o valor alto: '))
baixo = int(input('Informe o valor baixo: '))
contador = 0
soma = 0
media = 0
for i in range(alto,baixo,-3):
    print(i-3)
    contador+=1
    soma+=i-3

media=soma/contador
print(f'A médida é {media}')

