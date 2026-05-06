# Questão 3: Cofre Numérico 

# Crie um programa que simule a tentativa de abrir um cofre. O código correto é 2024. O usuário deve tentar digitar a senha.
# Se o usuário errar, o programa deve dizer se a senha digitada é numericamente maior ou menor que a senha correta.
# O programa deve contar quantas tentativas foram feitas.
# Se o usuário chegar a 5 tentativas erradas, o programa deve exibir "Acesso Bloqueado" e encerrar. Caso acerte antes, exibir "Cofre Aberto!".
import os
tentativas = 0
senha = 2024
while True:
    if(tentativas<5):
        getsenha = int(input('Informe a senha: '))
        tentativas+=1
        if(getsenha!=senha):
            if(getsenha<senha):
                os.system('cls')
                print('A senha é maior!')
            else:
                os.system('cls')
                print('A senha é menor!')
        else:
            print('Bem vindo meu caro!')
            break
    else:
        print('Você está bloqueado!')
        break
print(f'Tentivas: {tentativas}')
