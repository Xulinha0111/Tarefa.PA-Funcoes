#------- Exercício 2 --------#
""" 
Autor: Julia Bellini Sorrente
Data: 02/09/2022 10:40

"Crie um método que receba uma senha do usuário, caso a senha seja igual a 
“Senha123@” o método deve informar para o usuário: “Você está logado”. 
Caso não, deve informar: “Senha incorreta” e pedir a senha novamente."
"""

#--Função Senha--#
def Senha(chave):
        correta = "Senha123@"
        
#--Validação da Senha--#
        if (chave != correta):
            print("Senha incorreta. Tente novamente")
            
        else:
            print("Você está logado.")
            
#--Recepção da Senha--#
senha_us = input("Digite a Senha: ")
Senha(senha_us)

