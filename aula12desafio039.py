# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar;
# Se é hora de se alistar;
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoAtual = date.today().year
anoNascimento = int(input('Digite o ano do seu nascimento. Ex.: 1992 '))
idade = anoAtual - anoNascimento

if idade == 18:
    print('Você tem {} anos e está na hora de se alistar!'.format(idade))

elif idade < 18:
    print('Você tem {} anos e ainda irá se alistar em {} ano(s).'.format(idade, 18 - idade))
    print('Seu alistamento será em {}.'.format(anoAtual + (18-idade)))
else:
    print('Você tem {} anos e já passou {} ano(s) do seu alistamento!'.format(idade, idade - 18))
    print('Seu alistamento foi em {}.'.format(anoAtual - (idade - 18)))
