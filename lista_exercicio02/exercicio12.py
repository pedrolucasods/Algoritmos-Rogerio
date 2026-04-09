# 12. Faça um algoritmo que leia 5 números e imprima quantos números menores que
# 17 e maiores que 10 foram digitados.
maior10 = 0
menor17 = 0
for i in range(5):
    valor = int(input('Informe um valor:'))
    if(valor<17):
        menor17 +=1
        if(valor>10):
            maior10 +=1
print(f"Quantidade maior que 10: {maior10}\nQuantidade menor que 17: {menor17}")