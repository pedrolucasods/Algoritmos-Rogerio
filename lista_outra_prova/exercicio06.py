# Questão 6: Analisador de Triângulos

# Escreva um programa que receba três valores reais representando os lados de um triângulo e um quarto valor representando o maior ângulo interno em graus. O programa deve:

# Verificar a Existência: Um triângulo só existe se a soma de dois lados for sempre maior que o terceiro. Caso não exista, exiba "Medidas Inválidas" e encerre.
# Classificar por Lados: Se existir, informe se é Equilátero (3 lados iguais), Isósceles (2 iguais) ou Escaleno (todos diferentes).
# Classificar por Ângulos: Utilizando o valor do ângulo fornecido, informe se o triângulo é Retângulo (exatamente 90°), Obtusângulo (maior que 90°) ou Acutângulo (menor que 90°).

ladoA = int(input('Informe o lado 1: '))
ladoB = int(input('Informe o lado 2: '))
ladoC = int(input('Informe o lado 3: '))
existe = False
tipo = ''
tipoAngulo = ''
angulo = int(input('Informe o valor do angulo: '))

if(ladoA+ladoB)>ladoC:
    existe = True

if(existe):
    if(ladoA==ladoB) and (ladoA==ladoC):
        tipo='Equilatero'
    elif(ladoA == ladoB or ladoA == ladoC or ladoC == ladoB):
        tipo='Isóceles'
    else:
        tipo='Escaleno'

    if(angulo == 90):
        tipoAngulo='Retângulo'
    elif(angulo>90):
        tipoAngulo = 'Obtusângulo'
    elif(angulo<90):
        tipoAngulo = 'Acutângulo'

    print(f"Tipo de triangulos: {tipo}\nTipo de angulo: {tipoAngulo}")
else:
    print("O triangulo não existe")

