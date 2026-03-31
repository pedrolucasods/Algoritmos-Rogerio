codigo = int(input('Informe o código: '))
if (codigo == 1):
    print('Procedência: Sul')
elif (codigo == 2):
    print('Procedência: Norte')
elif (codigo == 3):
    print('Procedência: Leste')
elif (codigo == 4):
    print('Procedência: Oeste')
elif (codigo == 5) or (codigo == 6):
    print('Procedência: Nordeste')
elif (codigo >= 7) and (codigo <= 9):
    print('Procedência: Sudeste')
elif (codigo >= 10) and (codigo <= 20):
    print('Procedência: Centro-Oeste')
elif (codigo >= 21) and (codigo <= 30):
    print('Procedência: Nordeste')
else:
    print('Procedência inválida')

