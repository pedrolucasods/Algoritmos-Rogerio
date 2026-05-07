# Crie um programa em Python que peça ao usuário um número inteiro. 
# O programa deve imprimir uma estrutura triangular de números onde a primeira linha mostra apenas o número 1, 
# a segunda linha os números 1 e 2, e assim por diante, até a N-ésima linha.

# ·       Exemplo de saída se N=4:
valor = int(input('Informe um valor: '))
mensagem = ''
for i in range(valor):
    for j in range(i+1):
        if(j+1==1):
            print(i+1)
        if(i+1==valor):
            break
        print(j+1, end="")
        
