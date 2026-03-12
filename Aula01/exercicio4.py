"""
4. Faça um programa que receba 4 números inteiros positivos,
calcule a média desses números e imprima o resultado na tela
Exemplo: Entradas: 2, 5, 15, 13
"""

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))
valor3 = int(input("Informe o terceiro valor: "))
valor4 = int(input("Informe o quarto valor: "))

soma = valor1+valor2+valor3+valor4
media = soma/4

print(f"A media é: {media}")