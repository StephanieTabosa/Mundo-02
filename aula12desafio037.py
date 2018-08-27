# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

print('+~'*11)
print('Sua base de conversão!')
print('+~'*11)

numero = int(input('Digite um número inteiro: '))
conversao = int(input(' 1 -> converter para BINÁRIO\n 2 -> converter para OCTAL\n 3 -> converter para HEXADECIMAL'
                      '\nPara qual base você gostaria de converter? '))

if conversao == 1:
    print('Você escolheu o número {} e na base binária é {}.'.format(numero, bin(numero)[2:]))

elif conversao == 2:
    print('Você escolheu o número {} e na basa octal é {}.'.format(numero, oct(numero)[2:]))

elif conversao == 3:
    print('Você escolheu o número {} e na base hexadecimal é {}.'.format(numero, hex(numero)[2:]))

else:
    print('Opção inválida. Tente novamente.')
