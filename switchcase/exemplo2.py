numero = 2
match numero:
    case n if n<0:
        print("Número negativo")
    case n if n%2 == 0:
        print(f'{n} é um número par positivo')
    case n:
        print(f'{n} é um número ímpar positivo')