v = float(input('Qual a velocidade que o seu carro rodou? '))
u = v - 80
m = u * 7
if v > 80:
    print('Você ultrapassou o limite em {}km, sendo assim irá pagar uma múlta de R${}'.format(u,m))