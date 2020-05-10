'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. '''

#importa o módulo math, para que possa usar a função math.ceil para arredondar o número para cima
import math

area_m = float(input('Digite o valor em metros da área a ser pintada: '))

litros = area_m / 3
lata = float(litros / 18)
val_latas = float(lata * 80)

print(f'O número de latas de tinta utilizadas é {math.ceil(lata)}')
print(f'O preço total é de {math.ceil(val_latas)}')