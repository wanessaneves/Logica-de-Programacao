d = float(input('Qual será a distancia percorrida em km?'))
if d <= 200:
    print('O valor da sua viagem irá custar R${}'.format(d*0.50))
else:
    print('O valor da sua viagem vai custar R${}'.format(d*0.45))
