#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

#Pede o valor da nota de cada bimestre ao usuário
nota1 = float(input('digite o valor da primeira nota bimestral '))
nota2 = float(input('digite o valor da segunda nota bimestral '))
nota3 = float(input('digite o valor da terceira nota bimestral '))
nota4 = float(input('digite o valor da quarta nota bimestral '))

#calcula a média
media = (nota1 + nota2 + nota3 + nota4)/4

#Imprime o valor da média dos 4 bimestres
print('A média do aluno nos 4 bimestres é: ', +media)
