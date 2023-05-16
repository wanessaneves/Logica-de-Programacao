t = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
decimo = t + (10 -1) * r

for c in range(t, decimo + r ,r):
    print(c)
