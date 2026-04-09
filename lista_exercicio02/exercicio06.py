# 6. Escreva um algoritmo para ler um valor e escrever a mensagem “É MAIOR
# QUE 10!” se o valor lido for maior que 10, ou escrever “NÃO É MAIOR QUE
# 10!” caso contrário.
valor = int(input('Informe um valor: '))
if(valor>10):
    print('É MAIOR QUE 10!')
elif(valor<10):
    print("É MENOR QUE 10")
else:
    print("É IGUAL")
