# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('\033[33m*-*\033[m'*8)
print('\033[7;32m\033[1mSimulação de Empréstimo\033[m')
print('\033[33m*-*\033[m'*8)

valorCasa = float(input('Digite o valor da casa (sem pontos/vírgulas/traços): R$ '))
valorSalario = float(input('Digite o valor do seu salário: R$ '))
anos = int(input('Em quantos anos gostaria de pagar? '))
valorPrestacao = valorCasa / (anos * 12)

if valorPrestacao > 30/100*valorSalario:
    print('Infelizmente não será possível realizar o empréstimo.\n'
          'O valor da prestação é R$ {:.2f} e seu limite é R$ {:.2f}.'.format(valorPrestacao, 30/100*valorSalario))

else:
    print('Parabéns! Seu empréstimo foi concedido!')
