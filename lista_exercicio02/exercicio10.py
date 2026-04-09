# 10. Uma pessoa é obrigada a realizar o alistamento no exército brasileiro se for do
# sexo masculino e tiver 18 anos. Faça um programa que verifique se o usuário do
# seu programa precisará passar pelo processo de alistamento ou não.
sexo = input('Digite M para masculo ou F para feminino: ')
if(sexo.lower() == 'm'):
    print('Precisará passar pelo processo de alistamento!')
elif(sexo.lower() == 'f'):
    print('Não precisará passar pelo processo!')
else:
    print('Inválido')
