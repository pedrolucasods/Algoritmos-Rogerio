# 5. Faça um algoritmo que leia 5 números e imprima quantos números maiores que
# 100 foram digitados.
contador = 0
for i in range(5):
    numero = int(input('Informe um valor: '))
    if (numero>100):
        contador+=1

print(f"Quantidade números maior que 100: {contador}")