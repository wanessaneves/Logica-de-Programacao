from random import randint
computador = randint(0,10)
print('SOU SEU COMPUTADOR, ACABEI DE PENSAR EM UM NÚMERO ENTRE 0 E 10')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?'))
    tentativas += 1
    if jogador == acertou:
        acertou = True
print('Você ACERTOU com {} tentativas!'.format(tentativas))