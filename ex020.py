cidade = input('Digite a sua cidade natal: ').strip()

cidade1 = cidade.split()
print('Sua cidade começa com o nome Santo? {}'.format(cidade1[0].upper() == 'SANTO'))

