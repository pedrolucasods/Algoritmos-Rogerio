# 8. Escreva um algoritmo para ler o ano atual e o ano de nascimento de uma pessoa. 
# Escrever uma mensagem que diga se ela poderá ou não votar este ano.
nascimento = int(input('Informe seu ano de nascimento: '))
atual = 2026
idade = 2026 - nascimento
if(idade>=16):
    print("PODE VOTAR!")
else:
    print('NÃO PODE VOLTAR')
