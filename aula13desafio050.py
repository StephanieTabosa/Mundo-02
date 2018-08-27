# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o

s = 0
for num in range(0, 6):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        s += numero
        print(num)











