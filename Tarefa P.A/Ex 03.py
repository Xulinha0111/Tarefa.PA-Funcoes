#------- Exercício 3 --------#
""" 
Autor: Julia Bellini Sorrente
Data: 09/09/2022 18:35

Crie uma função que receba como parâmetros preenchidos pelo usuário, 
os valores dos lados de um triângulo e classifique como 
"Equilátero, Escaleno ou Isósceles".
"""
#--Pedindo informações ao Usuário--#
lado1 = float(input("Digite a medida do 1° Lado: "))
lado2 = float(input("Digite a medida do 2° Lado: "))
lado3 = float(input("Digite a medida do 3° Lado: "))

#--Definindo Função referente aos Triângulos--#
def Tipos(L1, L2, L3):

    #--Definindo se é ou não um Triângulo--#
    if lado1< lado2+lado3 and lado2< lado1+lado3 and lado3< lado1+lado2:
        print("É um triângulo... ")

        #--Definindo o Tipo de Triângulo--#
        if lado1 == lado2 == lado3:
            print("EQUILÁTERO!")
    
        elif lado1 != lado2 != lado3:
            print("ISÓSCELES!")

        else:
            print("ESCALENO!")
    else:
        print("Não é um triângulo. Tente novamente.")

#--Invocando a Função e Devolução de Dados ao Usuário--#
Tipos(lado1, lado2, lado3)