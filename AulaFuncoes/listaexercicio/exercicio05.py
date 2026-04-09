# Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito
# quando ele é igual a soma dos seus divisores excetuando ele próprio. (Ex: 6 é perfeito,
# 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar o valor inteiro 1 para
# verdadeiro e 0 caso contrário.

def perfeito(n):
    soma = 0
    for i in range(n):
        if(i==0):
            pass
        else:
            if(n%i == 0):
                soma += i
    if(soma == n):
        return 1
    else:
        return 0

print(perfeito(28))

