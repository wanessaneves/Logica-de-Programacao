produtos = ('pão', 3.50, 'Arroz', 6.75, 'Feijão', 8.00, 'Ovo', 5.00, 'sabão', 8.90, 'ração', 75.00)
print('='*40)
print(f'{"TABELA":^40}')
print('='*40)
for pos in range(0,len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}',end= '')
    else:
        print(f'{produtos[pos]:.>5}')
print('='*40)


