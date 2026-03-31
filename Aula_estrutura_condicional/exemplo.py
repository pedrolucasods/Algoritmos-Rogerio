operador_1 = int(input('informe um valor: '))
if operador_1 % 2 == 0:
    print(operador_1/2)
    print("O número é par")
else:
    print("O número é impar")

## operador ternários
idade = 16
result = "É maior de idade" if idade>=18 else "É menor de idade"
print(result)