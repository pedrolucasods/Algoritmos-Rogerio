idade = int(input('informe sua idade: '))

if (idade>=5) and (idade<=7):
    print('Categoria: infantil')
elif (idade>=8) and (idade<=10):
    print('Categoria: juvenil')
elif (idade>=11) and (idade<=15):
    print('Categoria: adolescente')
elif (idade>=16) and (idade<=30):
    print('Categoria: adulto')
elif (idade>30):
    print('Categoria: sênior')
else:
    print('Você não se encaixar em nenhuma categoria')