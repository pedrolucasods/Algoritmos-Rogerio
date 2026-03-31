# Faça um programa que leia um número inteiro e diga se este número é menor que
# zero, igual a zero ou maior que zero

valor = int(input('Informe um valor: '))
if valor<0:
    print('Valor é menor que zero')
elif valor == 0:
    print('Valor é igual a zero')
elif valor > 0:
    print('Valor é maior que zero')