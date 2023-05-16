import random
n = random.randint(1,20)
u = int(input('Digite um valor de 1 a 20: '))
if u == n:
    print('O número que você digitou foi igual ao que o computador escolheu: {}'.format(u))
else:
    print('Os números foram diferentes, o seu foi {} e o do PC foi {}'.format(u,n))

