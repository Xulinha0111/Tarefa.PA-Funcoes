#------- Exercício 4 --------#
""" 
Autor: Julia Bellini Sorrente
Data: 09/09/2022 11:35

"Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair. 
Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida."
"""

#--Definindo as Funções--#
def Soma(n1, n2):
    return n1 + n2

def Sub(n1, n2):
    return n1 - n2

def Div(n1, n2):
    return n1 / n2

def Mult(n1, n2):
    return n1 * n2

#--Pedindo valores ao Usuário--#
x = float(input("Valor 1: "))
y = float(input("Valro 2: "))

#--Painel de Opções--#
while True:
    operacao = int(input(
    "---------------\nDigite a ação desejada: \n1: Soma \n2: Subtração \n3: Divisão \n4: Multiplicação \n5: Saída \n---------------\n-->: "
    ))

#--Devolução das Funções e Resultados--#
    if operacao == 1:
        resultado = Soma(x, y)
        print("O resultado da SOMA é: ",resultado)

    elif operacao == 2:
        resultado = Sub(x, y)
        print("O resultado da SUBTRAÇÃO é: ", resultado)
    elif operacao == 3:
        resultado = Div(x, y)
        print("O resultado da DIVISÃO é: ", resultado)
    elif operacao == 4:
        resultado = Mult(x, y)
        print("O resultado da MULTIPLICAÇÃO é: ", resultado)

    elif operacao == 5:
        break