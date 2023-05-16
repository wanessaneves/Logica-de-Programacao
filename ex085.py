from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = list()
print('-='*25)
print('Valores sorteados: ')
for k, v in jogo.items():
    sleep(1)
    print(f'O {k} sorteou o número {v} no dado')
print('-='*25)
ranking = sorted(jogo.items(), key = itemgetter(1),reverse = True)
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
print('-='*25)



