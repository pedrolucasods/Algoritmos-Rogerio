# 9. Para doar sangue uma pessoa precisa ter entre 18 e 69 anos e pesar no mínimo
# 50 kg. Faça um programa que pergunte a idade e o peso do usuário e verifique se
# ele pode doar sangue.
idade = int(input('Informe sua idade: '))
peso = int(input('Informe seu peso: '))
if((idade>=18 and idade<=69) and (peso>=50)):
    print('Pode doar sangue!')
else:
    print('Não pode doar sangue!')