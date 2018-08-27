# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input('Digite o seu peso (em Kg): '))
altura = float(input('Qual a sua altura (em metros)? Ex: 1.71: '))
imc = peso / (altura * altura) #ou (altura**2)

print('Seu IMC é {:.1f}.'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO do peso! Cuide-se')

elif 18.5 <= imc < 25:
    print('\033[36mPARABÉNS!\033[m Você está no peso ideal!')

elif 25 <= imc < 30:
    print('Você está na categoria SOBREPESO. Cuide-se')

elif 30 <= imc <= 40:
    print('Você está na categoria OBESIDADE! Cuide-se.')

else:
    print('CUIDADO! Você está na categoria OBESIDADE MÓRBIDA. Cuide-se')

