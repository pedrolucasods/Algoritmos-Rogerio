conceito = ''
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a primeira nota: '))
nota3 = float(input('Informe a primeira nota: '))

soma = nota1+nota2+nota3
media = soma/3
if(media>=8 and media<=10):
    conceito = 'A'
elif(media == 7):
    conceito = 'B'
elif(media == 6):
    conceito = 'C'
elif(media == 5):
    conceito = 'D'
elif(media>=0 and media<5):
    conceito = 'E'
print(f'Sua média é {media}, conceito é {conceito}')
