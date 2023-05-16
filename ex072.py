palavras = ('casa','bola','mala','programação','desenvolvimento','paisagem')
vogais = ''
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for l in p:
        if l in 'aeiou':
            print(l, end=' ')