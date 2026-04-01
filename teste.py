valor = int(input('informe: '))
resultado = 0
mensagem = ''
for i in range(valor):
    msg = f'{i}+{1}'
    mensagem += f'{msg}/'
    resultado+=i+1

print('Soma=',mensagem,'= ',resultado)
