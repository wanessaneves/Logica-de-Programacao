from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando cinco valores da lista -> ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        sleep(1)
    print('PRONTO!')

def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares da lista: {lista}, temos como resultado {soma}')



numeros = list()
sorteia(numeros)
somapar(numeros)
