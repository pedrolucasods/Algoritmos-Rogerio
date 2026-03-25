idade = int(input('Informe sua idade: '))
match idade:
    case  idade if (idade >= 5) and (idade <=7):
        print('Categoria: infantil')
    case idade if (idade >= 8) and (idade<=10):
        print('Categoria: juvenil')
    case idade if (idade >= 11 ) and (idade<=15):
        print('Categoria: adolescente')
    case idade if (idade >=16) and (idade<=30):
        print('Categoria: adulto')
    case idade if (idade>30):
        print('Categoria: sênior')
    case _:
        print('Você não se encaixa em nehuma categoria')




