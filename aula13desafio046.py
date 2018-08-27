# Faça um programa que mostre na tela uma contagem regressiva para estouro de fogos de artifício, indo de 10 até 0
# com uma pausa de 1 segundo entre eles

from time import sleep
from emoji import emojize
from datetime import date
ano = date.today().year + 1

print('{:^60}'.format(emojize('\033[33;41m:fireworks: :fireworks:\033[m \033[1;33;46mVAI COMEÇAR A CONTAGEM REGRESSIVA PARA O ANO NOVO\033[m \033[33;41m:fireworks: :fireworks:\033[m')))
sleep(2)

for c in range(10, 0, -1):
    sleep(1)
    print(c)

sleep(2)
print(emojize('\033[33m:fireworks: :fireworks:\033[m FELIZ ANO NOVO, FELIZ {} \033[33m:fireworks: :fireworks:\033[m!!!'.format(ano), use_aliases=True))


