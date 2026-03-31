# Elabore um programa que receba dois números reais (números com casas
# decimais) e permita que o usuário escolha qual operação ele deseja fazer: adição,
# subtração, divisão, multiplicação, raiz quadrada ou resto da divisão (similar a uma
# calculadora básica).
import math

print('=== Calculadora ===')
print('Soma = +\nSubtracao = -\nMultiplicacao = *\nDivisão = /\nRaiz = raiz\nResto da divisão = %')
valor1 = int(input('Informe um valor: '))
sinal = input('Informe a operação: ')
valor2 = int(input('Informe um valor: '))
operacao = sinal.lower()
if(operacao == '+'):
    resultado = valor1 + valor2
elif(operacao == '-'):
    resultado = valor1 - valor2
elif(operacao == '*'):
    resultado = valor1 * valor2
elif(operacao == '/'):
    resultado = valor1/valor2
elif(operacao == 'raiz'):
    resultado = 
