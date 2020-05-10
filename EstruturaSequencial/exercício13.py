'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    a) Para homens: (72.7*h) - 58
    b) Para mulheres: (62.1*h) - 44.7 
'''

#Pede para o usuário digitar a altura e atribui o valor a variável h
h = float(input('Digite sua altura: '))

#Pergunta qual o sexo da pessoa
sexo = input('Você é "homem" ou "mulher" ')

#Condicional para efetuar o cálculo do peso ideal. Se for homem executa a fórmula para homem e se for mulher executa a fórmula para mulher

if sexo == 'homem':
    homem = (72.7 * h) -58
    print(f'Seu peso ideal é: {homem}')
else:
    mulher = (62.1 * h) - 44.7
    print(f'Seu peso ideal é: {mulher}')


