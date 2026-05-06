# Questão 2: Clube de Leitura 

# O programa deve ler o Nome, Quantidade de Livros Lidos no Ano e Gênero Favorito (Ficção/Não-Ficção) de 6 participantes. Ao final, informe:

# O total de livros lidos por todo o grupo.
# A porcentagem de pessoas que preferem "Ficção".
# Quantos participantes preferem "Não-Ficção".
import os

quantidade = 0
porcentagem = 100/6
contFiccao = 0
laco = 6
for i in range(laco):
    os.system('cls')
    nome = input('Informe seu nome: ')
    quantidadeLivro = int(input('Informe a quantidade de livros lidos: '))
    quantidade+=quantidadeLivro
    generoLivro = int(input('1 - Ficção\n2 - Não Ficção\nInforme seu gênero favorito: '))
    # if(generoLivro!=1 and generoLivro!=2):
    #     print('Erro, você digitou um genero inválido.\nPreenche novamente os dados!\n')
    #     nome=''
    #     quantidadeLivro=0
    #     laco+=1
    if(generoLivro == 1):
        contFiccao+=1

os.system('cls')
porcentagemDeFiccao = (contFiccao*porcentagem)
quantidadeNaoFiccao = laco-contFiccao
print(f'Quantidade de livros lidos: {quantidade}\nPorcentagem de ficção: {porcentagemDeFiccao:,.2f}%\nQuantidade de Nâo Ficção: {quantidadeNaoFiccao}')
    

    

