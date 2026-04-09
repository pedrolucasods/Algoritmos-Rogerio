# 7. Escreva um algoritmo para ler um valor e escrever a mensagem “É PAR!” se o
# valor lido for par, ou escrever “É ÍMPAR!” caso contrário.
valor = int(input('Informe um valor: '))
if(valor%2 == 0):
    print('É PAR')
else:
    print('É IMPAR')
