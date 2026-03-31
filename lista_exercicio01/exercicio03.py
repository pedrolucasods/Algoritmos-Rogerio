# Os pares de instruções abaixo produzem o mesmo resultado?
# a. a = (4/2) + (2/4) e a = 4/2 + 2/4
# b. b = (4 + 2) * 2 - 4 e b = 4+2*2-4

a1 = (4/2) + (2/4)
a2 = 4/2 + 2/4
if a1 == a2:
    print('O par A contem os mesmos resultados')
else:
    print('O par A não contem os mesmos resultados')
b1 = (4 + 2) * 2 - 4
b2 = 4+2*2-4
if b1 == b2:
    print('O par B possuiem os mesmos resultados')
else:
    print('O par B não possuem o mesmo resultado')

#resposta
# O par A tem o mesmo resultado, o par B não tem
