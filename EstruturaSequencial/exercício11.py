'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

int1 = int(input('Digite um número inteiro: '))
int2 = int(input('Digite outro número inteiro: '))
real1 = float(input('Digite um número real: '))

resultado1 = (2 * int1) * (int2 / 2)
resultado2 = (3*int1) + real1
resultado3 = real1 ** 3

print(f'o produto do dobro do primeiro com metade do segundo é igual a {resultado1}')
print(f'a soma do triplo do primeiro com o terceiro é igual a {resultado2}')
print(f'o terceiro elevado ao cubo é igual a {resultado3}')
