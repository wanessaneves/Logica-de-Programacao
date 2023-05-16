n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
if m <= 6 :
    print('Sua nota final é {}, você está abaixo da média, estude um pouco mais da próxima vez'.format(m))
elif 8 > m > 6:
    print('Parabéns! você está na área de aprovação, sua nota final foi {}'.format(m))
else:
    print('Excelente! Você conquistou uma nota {}'.format(m))
