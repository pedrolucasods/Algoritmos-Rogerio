# Faça uma função que recebe um valor inteiro e verifica se o valor é
# par ou ímpar. A função deve retornar um valor inteiro.

def verificar(numero):
    if(numero%2 == 0):
        return 2
    else:
        return 3
    
print(verificar(5))