from random import randint
num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os números sorteados foram: ')
for n in num:
    print(f'{n}')
print(f'O maior valor foi {max(num)}')
print(f'E o menor valor foi {min(num)}')


