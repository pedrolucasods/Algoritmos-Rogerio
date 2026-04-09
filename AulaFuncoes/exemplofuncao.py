# def mostrar_disciplina():
#     print("Algoritmos")

# mostrar_disciplina()

# def mostar_disciplina(nome, curso):
#     print(f"Disciplina: {nome}! Do curso {curso}")

# mostar_disciplina("Algoritmos","TADS")
# mostar_disciplina("Banco de Dados","TADS")

# resultado =  0

# def somar(val1,val2):
#     resultado = val1+val2
#     print(resultado)

# def mostar_resultado():
#     print(resultado)


# valor1 = input('Informe um valor: ')
# valor2 = input('Informe um valor: ')
# somar(int(valor1), int(valor2))

# def realizar_prova(tentativas=3, tempo=30):
#     print(f"Foram: {tentativas} tentativas no tempo de {tempo} minutos.")

# realizar_prova()
# realizar_prova(2)
# realizar_prova(2,120)

def calcular_dobro(n):
    return n*2 #return devolver algo para quem chamar a função

# def calcular_dobro(n:int) -> int:
#     return n*2


resultado = calcular_dobro(7)
print(f"O dorbo é: {resultado}")