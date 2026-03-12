print("Hello world")


#Isso é um comentário
#ctrl + k +c = comenta ou ctrl + / ou ctrl + ;

""" - String Docs
é comentário
tudo 
que estiver no meio
"""

#Toda variável pode ter letras e números


# Tipos de váriaveis
valor1 = 3 #int
nome = "Pedro" #string
valor2 = 2.2 #float
boleano = True #booleano True e False

#Operações
numero1 = 2
numero2 = 3

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print('a soma é:', soma)

print("Ola mundo!\npula uma linha.")
#\n pula uma linha
print("Primeira linha")
print()
print("Segunda linha")

preco = 49.90
desconto = 0.10

#posso indicar o tipo de dados que a varável vai aceitar
nome: str="Pedro"
idade: int = 19

nome = "Pedro"
idade = 19

# Métodos de impressão

#Com f-string (moderno e limpo)
print(f"Olá, {nome}. Você tem {idade} anos.")

#Sem f-string (antigo)
#Concatenação(+)
print("Olá, "+ nome + ". Você tem " + str(idade) + "anos")

#Vírgulas no print
print("Olá,", nome,". Você tem", idade,"anos")

#Método .format()
print("Olá {}. Você tem {} anos".format(nome,idade))

#Conta
preco = 10
quantidade = 3
print(f"O total da compra é: R${preco*quantidade}")

#Entrada de dados
print("\nEntrada de dados\n")
#nome = input("Digite o seu nome: ")
#valor = int(input("Digite sua idade: "))
#valor = float(input("Digite o valor: "))

#print(valor)


#Operadores


