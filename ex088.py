galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [F/M]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F!')

    pessoa['idade'] = int(input('Qual sua idade? '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print(galera)
print('-='*30)
print(f'Ao todo foram cadastradas {len(galera)} pessoas')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f}')
print('A mulheres cadastradas foram: ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}')
print('As pessoas que estão acima da média foram: ')
for p in galera:
    if p['idade'] > media:
        print(f'{p["nome"]}')
print(' << ENCERRADO >>')
