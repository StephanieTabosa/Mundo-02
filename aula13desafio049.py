# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço 'for'

print('{:*^40}'.format(' TABUADA '))
tabuada = int(input('Qual tabuada gostaria de consultar? '))
for t in range(1, 10 + 1):
    mult = tabuada*t
    print('{} x {} = {}'.format(tabuada, t, mult))

