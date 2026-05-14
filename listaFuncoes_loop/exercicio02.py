# Desenvolva um programa que simule as operações básicas de um
# caixa eletrônico. O cliente começa com um saldo de R$ 0,00. O
# programa deve exibir um menu contínuo com as seguintes regras:
# • O menu deve ter 4 opções: Ver Saldo, Depositar, Sacar e Sair.
# • Crie uma função para o depósito e outra para o saque. Ambas
# devem receber o saldo atual e o valor da operação. Obs:
# devem retornar o saldo atualizado.
# • A função de saque não pode permitir que o usuário saque um
# valor maior do que ele tem na conta (deve exibir uma
# mensagem de erro).
# • Valores de depósito e saque não podem ser negativos
import os

def minhaconta():
    saldo = 0
    while True:
        print('#### Minha conta ####')
        print("1- Ver Saldo\n2- Depositar\n3- Sacar\n4- Sair")
        opcao = int(input('Informe uma opção: '))

        # exibir saldo
        if(opcao == 1):
            os.system('cls')
            print(f"Saldo: R${saldo}")

        # depositar
        elif(opcao == 2):
            addSaldo = float(input('Informe o valor: '))
            deposito = depositar(saldo,addSaldo)
            if(not deposito):
               os.system('cls')
               print('Erro ao adicionar a conta!')
            else:
                os.system('cls')
                saldo = deposito
                print(f"Foi adicionar R${addSaldo} a sua conta!")

        # sacar
        elif(opcao == 3):
            removeSaldo = float(input('Informe o valor do saque: '))
            saque = sacar(saldo,removeSaldo)
            if(not saque):
                os.system('cls')
                print("Erro ao sacar!")
            else:
                os.system('cls')
                saldo = saque
                print(f"Você sacou R${removeSaldo} da sua conta!")

        # sair
        elif(opcao == 4):
            os.system('cls')
            print("Deletando conta do banco...")
            break

        # tratando opções inválidas
        else:
            os.system('cls')
            print("Opção inválida")

def depositar(saldo,adicionar):
    if(adicionar<1):
        return False
    return saldo+adicionar

def sacar(saldo,retirar):
    if(retirar>saldo or retirar<1):
        return False
    else:
        return saldo-retirar
    
minhaconta()




