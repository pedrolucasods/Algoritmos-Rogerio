# Faça um programa que leia três valores (representam os lados de um triangulo) e 
# verifique se o triângulo é um equilátero (os três lagdos são iguais),
# um isóceles(dois lados são iguais) ou escaleno (os três lados são diferentes)
ladoA = int(input('Informe o valor do lado A: '))
ladoB = int(input('Informe o valor do lado B: '))
ladoC = int(input('Informe o valor do lado C: '))

if (ladoA == ladoB) and (ladoB == ladoC):
    print('O triangulo é Equilátero')
elif (ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
    print('O triangulo é Isóceles')
elif (ladoA != ladoB) and (ladoA != ladoC) and (ladoB != ladoC):
    print('O triângulo é Escaleno')