# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Media 7.0 ou superior: APROVADO

from time import sleep

print('\033[31m+-\033[m'*11)
print('CALCULANDO SUA MÉDIA')
print('\033[31m+-\033[m'*11)

nota1 = float(input('Qual foi a primeira nota? '))
nota2 = float(input('Qual foi a segunda nota? '))
media = (nota1 + nota2)/2
print('Processando sua solicitação...')
sleep(3)
if media < 5.0:
    print('Você foi \033[31mREPROVADO\033[m!')

elif 5.0 <= media <= 6.9:
    print('Você está de \033[36mRECUPERAÇÃO\033[m. Estude!')

elif media >= 7.0:
    print('Parabéns, você está \033[32mAPROVADO\033[m!!!')

else:
    print('Erro na operação')



