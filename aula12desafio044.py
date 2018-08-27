# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal, condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS STÈPHANIE '))
valorProduto = float(input('Qual o valor do produto? R$ '))
print('Escolha uma opção de pagamento:\n\n'
      '[1] À vista dinheiro/Cheque\n'
      '[2] À vista no cartão\n'
      '[3] Em até 2x no cartão\n'
      '[4] Em 3x ou mais no cartão')

pagamento = int(input('Qual a opção de pagamento? '))

if pagamento == 1:
    preco = valorProduto - (10/100*valorProduto)
    print('O produta custa R$ {:.2f}, mas à vista dinheiro/cheque custará R$ {:.2f}.'.format(valorProduto, preco))

elif pagamento == 2:
    preco = valorProduto - (5/100*valorProduto)
    print('O produto custa R$ {:.2f}, mas à vista no cartão custará R$ {:.2f}.'.format(valorProduto, preco))

elif pagamento == 3:
    print('O produto custa R$ {:.2f} e custará R$ {} de acordo com a opção escolhida.'.format(valorProduto, valorProduto))
    parcelas = valorProduto / 2
    print('Serão 2x de R$ {} SEM JUROS.'.format(parcelas))

elif pagamento == 4:
    totparc = int(input('Em quantas parcelas? '))
    preco = valorProduto + (20/100*valorProduto)
    print('O produto custa R$ {:.2f}, mas em {}x no cartão custará R$ {:.2f}.'.format(valorProduto, totparc, preco))
    parcelas = (valorProduto + (20/100*valorProduto)) / totparc
    print('Serão {}x de R$ {:.2f} COM JUROS.'.format(totparc, parcelas))
else:
    print('Opção inválida. Tente novamente.')
