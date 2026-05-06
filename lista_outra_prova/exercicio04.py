# Questão 4: Supermercado

# Escreva um programa que peça ao usuário para digitar o preço de diversos produtos vendidos. O programa deve parar quando o usuário digitar o valor 0. Ao final, o programa deve exibir:
# O total de itens cadastrados.
# O valor total da compra.
# A média de preço dos produtos.
# Quantos produtos custam mais de R$ 50,00.

quantidade = 0
soma = 0
maior50 = 0
while True:
    preco = float(input('Informe o preço do produto ou digite 0 ou negativo para parar: '))
    if(preco == 0 or preco<0):
        break
    quantidade+=1
    soma+=preco
    if(preco>50):
        maior50+=1
media = soma/quantidade
print(f'Quantidade: {quantidade}\nMaior que 50:{maior50}\nTotal: {soma}')