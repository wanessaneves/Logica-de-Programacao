n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1
print('Calculando {}!'.format(n))
while c > 0:
    print('{}'.format(c), end=' ')
    print('X' if c > 1 else '=', end= ' ' )
    f = f * c
    c-=1
print('{}'.format(f))
