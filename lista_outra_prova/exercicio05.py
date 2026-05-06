# Crie um programa em Python que peça ao usuário um número inteiro. 
# O programa deve imprimir uma estrutura triangular de números onde a primeira linha mostra apenas o número 1, 
# a segunda linha os números 1 e 2, e assim por diante, até a N-ésima linha.

# ·       Exemplo de saída se N=4:
valor = int(input('Informe um valor: '))
mensagem = ''
for i in range(valor+1):
    # print(i+1)
    for j in range(i):
        print(f'{j+1}')
        valor= str(j+1)
        mensagem+=valor
    print(mensagem)
