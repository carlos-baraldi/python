#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input('Digite quanto você ganha por hora:'))
num_hora = float(input('Digite quantas horaas você trabalha no mês: '))

salario = ganho_hora * num_hora

print(f'Você ganha R${salario } de salário')
