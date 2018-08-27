# Crie um programa que faça o computador jogar JOKENPÔ com você

import emoji
import random
import time

print('+-*/'*9)
print(emoji.emojize('\033[31m:punch:\033[m \033[33m:wave: :v:\033[m \033[1;36m VAMOS JOGAR JOKENPÔ ? \033[m \033[34m:v: :wave:\033[m \033[35m:punch:\033[m', use_aliases=True))
print('+-*/'*9)

jogo = ['Pedra', 'Papel', 'Tesoura']

escolhaPessoa = str(input('Escolha uma opção (Pedra, Papel ou Tesoura): ')).capitalize()
print('Processando a sua escolha...')
time.sleep(2)

print(emoji.emojize('Agora eu vou escolher... :thought_balloon:', use_aliases=True))
time.sleep(2)

escolhaPC = random.choice(jogo)
print(escolhaPC)
print(emoji.emojize('Resultando chegando... :speech_balloon:',use_aliases=True))
time.sleep(2)

if 'Pedra' in escolhaPessoa and 'Papel' in escolhaPC:
    print('COMPUTADOR VENCEU !!!')

elif 'Papel' in escolhaPessoa and 'Pedra' in escolhaPC:
    print('JOGADOR VENCEU !!!')

elif 'Tesoura' in escolhaPessoa and 'Pedra' in escolhaPC:
    print('COMPUTADOR VENCEU !!!')

elif 'Pedra' in escolhaPessoa and 'Tesoura' in escolhaPC:
    print('JOGADOR VENCEU !!!')

elif 'Tesoura' in escolhaPessoa and 'Papel' in escolhaPC:
    print('JOGADOR VENCEU !!!')

elif 'Papel' in escolhaPessoa and 'Tesoura' in escolhaPC:
    print('COMPUTADOR VENCEU !!!')

elif escolhaPessoa == escolhaPC:
    print(emoji.emojize('EMPATAMOS :clap:!!!', use_aliases=True))

else:
    print('Você digitou algo errado. Tente novamente.')








