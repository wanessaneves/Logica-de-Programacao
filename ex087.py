jogador = dict()
partidas = list()
jogador['nome'] = input('Nome do jogador: ')
tot = int(input(f'Quantas partidas foram jogadas por {jogador["nome"]} : '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols foram feitos na {c + 1}° partida? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print('Jogador!')
print('-='*30)

for i, v in enumerate(jogador['gols']):
    print(f'Na {i + 1} ° partida {jogador["nome"]} fez {v} gols')
print(f'Totalizando {sum(jogador["gols"])} gols')