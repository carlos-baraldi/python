'''João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas. '''

#Pede para o usuário digitar o peso do total de peixes e atribui a variável peso
peso = float(input('Digite o peso do total de peixes (em KG): '))

#calcula quantos KGs foram excedidos e atribui a variável excesso
excesso = peso - 50

#calcula quanto será pago de multa e atribui a variável multa
multa = excesso * 4

if peso > 50:
    print(f'Você pescou {peso} KGs de peixe, excedeu o valor estabelecido pelo regulamento em {excesso} KGs e terá que pagar um valor de R${multa} ')
else:
    print('você não excedeu o valor estabelecido pelo regulamento')