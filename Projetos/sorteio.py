######################################################################################
'''
--Jogo onde o programa vai gerar um número aleatório e vai pedir para o usuário
adivinhar o número gerado.
--O usuário terá 4 tentativas para acertar o número
'''
######################################################################################
import random #precisa para poder gerar o número aleatório
import os # precisa para utilizar o comando de limpar a tela

erros = 0

total_erros = 3

numero_aleatorio = random.randrange(0, 10) # vai atribuir a variável um valor aleatório

num = 0


while (erros <= total_erros):
    num = int(input("Adivinhe qual número eu escolhi "))
    if (num == numero_aleatorio):
        print("------Parabéns, Você ACERTOU!------")
        break
    elif (num > numero_aleatorio):
        print(f'ERROU! Você digitou {num} e esse número é maior que o número que eu escolhi')
    elif(num < numero_aleatorio):
        print(f'ERROU! Você digitou {num} e esse número é menor que o número que eu escolhi')
    erros = erros + 1
    os.system("clear")
else:
    print(f'Você tentou {erros} vezes e não conseguiu adivinhar o número. =/')
    print(f'O número correto era o {numero_aleatorio}')

    
