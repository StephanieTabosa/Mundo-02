# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date
anoAtual = date.today().year
anoNascimento = int(input('Digite seu ANO de nascimento. Ex.: 1992: '))
idade = anoAtual - anoNascimento

if idade <= 9:
    print('Você tem {} anos e sua categoria é {}.'.format(idade, 'MIRIM'))

elif 9 < idade <= 14:
    print('Você tem {} anos e sua categoria é {}.'.format(idade, 'INFANTIL'))

elif 15 < idade <= 19:
    print('Você tem {} anos e sua categoria é {}.'.format(idade, 'JÚNIOR'))

elif idade == 20:
    print('Você tem 20 anos e sua categoria é {}.'.format('SÊNIOR'))

else:
    print('Você tem {} anos e sua categoria é {}.'.format(idade, 'MASTER'))






