#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numero = input('Digite um numero ') # Pede um número ao usuário, que é armazenado na variável numero
int(numero) # A função input sempre gera uma string, portanto usei a função int para transformar o número em inteiro
print('O número informado foi ' + numero) #imprime o valor do número informado
