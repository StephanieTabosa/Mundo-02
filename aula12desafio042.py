# Refaça o DESAFIO 035 acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes


print('-=-'*8)
print('Analisando um triângulo')
print('-=-'*8)
A = float(input('Qual o tamanho da primeira reta? '))
B = float(input('Qual o tamanho da segunda reta? '))
C = float(input('Qual o tamanho da terceira reta? '))

if (B - C) < A < B + C and (A - C) < B < A + C and (A - B) < C < A + B:
    print('É possível criar um triângulo com os valores fornecidos!')
    if A == B != C or A == C != B or B == C != A:
        print('Foi formado um triângulo ISÓSCELES.')
    elif A == B == C:
        print('Foi formado um triângulo EQUILÁTERO.')
    elif A != B != C != A:
        print('Foi formado um triângulo ESCALENO.')
else:
    print('Não será possível a criação de um triângulo!')




