# Faça um procedimento que recebe por parâmetro os valores necessários para o
# cálculo da fórmula de báskara e imprima as suas raízes, caso seja possível calcular.
import math

def baskara(a,b,c):
    delta = (b**2) - (4*a*c)
    print(delta)
    calcx1 = (-b + (math.sqrt(delta)))/2*a
    calcx2 = (-b - (math.sqrt(delta)))/2*a
    print(f"Resultado:\nX1 = {calcx1}\nX2 = {calcx2}")

baskara(1,-5, 6)