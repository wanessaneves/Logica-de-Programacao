def ficha(nome=str, gols=0):
    print('-=' * 15)
    print(f'Nome do jogador : {nome}.')
    print(f'Quantidade de gols: {gols}.')
    print('-=' * 15)

nome = str( input('Qual o seu nome? '))
gols = int( input('Quantos gols você realizou? '))
ficha(nome,gols)