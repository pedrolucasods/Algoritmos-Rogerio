# 13. Faça um algoritmo equivalente ao último exercício, isto é, que leia 5 números e
# imprima quantos números são maiores que 100, quantos números são menores
# que 17 e quantos números são menores que 17 e maiores que 100.
menor17 = 0
maior100 = 0
for i in range(5):
    valor = int(input('Informe um valor: '))
    if(valor<17):
        menor17+=1
    if(valor>100):
        maior100 += 1
print(f"Menor que 17 {menor17}\nMaior que 100:{maior100}")