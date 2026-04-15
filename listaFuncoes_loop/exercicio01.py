# Crie um programa que exiba um menu interativo para o usuário com
# opções de conversão de medidas.
# O programa deve rodar continuamente até que o usuário escolha a
# opção de sair.
# O menu deve ter 3 opções: Converter Celsius para Fahrenheit,
# Converter Metros para Centímetros e Sair.
# Crie uma função específica para cada cálculo de conversão.
# Se o usuário digitar uma opção que não existe, o programa deve
# avisar que a opção é inválida e mostrar o menu novamente.
def calculos():
    while True:
        print('######## Menu ########\n1 - Converter Celsiu para Fahrenheit\n2 - Converter Metros para centimetros\n3 - Sair')
        opcao = int(input('Informe uma opção: '))
        if(opcao == 1):
            celsiu = float(input('Informe a temperatura em celsius: '))
            farenheit = (celsiu*1.8)+32
            print(f"A temperatura {celsiu}º em Farenheit é {farenheit}\n")
        elif(opcao == 2):
            metros = float(input('Informe o metro: '))
            centimetros = metros *100
            print(f"A medida {metros}m é {centimetros}cm\n")
        elif(opcao == 3):
            print('Programa encerrado...')
            break
        else:
            print('Opção inválida\n')

calculos()
        
    