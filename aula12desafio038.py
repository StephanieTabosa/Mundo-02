# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior;
# O segundo valor é maior;
# Não existe valor maior, os dois são iguais.

print('\033[34m#\033[m'*20)
print('Qual o número maior?')
print('\033[34m#\033[m'*20)
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print('O primeiro número é maior!')

elif n2 > n1:
    print('O segundo número é maior!')

else:
    print('Os dois números são iguais!')
