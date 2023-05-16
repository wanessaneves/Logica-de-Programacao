import math
ang = int(input('Digite o ângulo: '))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))
print('A partir do ângulo {} digitado, o seno é de {:.2f} graus, o cosseno é de {:.2f} graus e a tangente é de {:.2f} graus'.format(ang,s,c,t))

