# Elabore um programa que receba dois números reais (números com casas
# decimais) e permita que o usuário escolha qual operação ele deseja fazer: adição,
# subtração, divisão, multiplicação, raiz quadrada ou resto da divisão (similar a uma
# calculadora básica).
import math

print('=== Calculadora ===')
print('Soma = +\nSubtracao = -\nMultiplicacao = *\nDivisão = /\nRaiz = raiz\nResto da divisão = %')
print('\n')
valor1 = int(input('Informe um valor: '))
sinal = input('Informe a operação: ')

operacao = sinal.lower()
if(operacao == '+'):
    valor2 = int(input('Informe um valor: '))
    resultado = valor1 + valor2
    print(f'Resultado: {resultado}')
elif(operacao == '-'):
    valor2 = int(input('Informe um valor: '))
    resultado = valor1 - valor2
    print(f'Resultado: {resultado}')
elif(operacao == '*'):
    valor2 = int(input('Informe um valor: '))
    resultado = valor1 * valor2
    print(f'Resultado: {resultado}')
elif(operacao == '/'):
    valor2 = int(input('Informe um valor: '))
    resultado = valor1/valor2
    print(f'Resultado: {resultado}')
elif(operacao == 'raiz'):
    resultado = math.sqrt(valor1)
    print(f'Resultado: {resultado}')
elif(operacao == '%'):
    valor2 = int(input('Informe um valor: '))
    resultado = valor1%valor2
    print(f'Resultado: {resultado}')
else:
    print('Operação inválida!')
