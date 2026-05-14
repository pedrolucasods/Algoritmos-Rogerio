# Faça uma função que recebe um valor inteiro e verifica se o valor é
# positivo ou negativo. A função deve retornar um valor inteiro.

def verificarNumero(numero):
    if(numero<0):
        return 1
    elif(numero>0):
        return 2
    else:
        return 0

print(verificarNumero(0))
