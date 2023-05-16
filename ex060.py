n = q = s = 0
n = (int(input('Digite um valor: ')))
while n != 999:
    s += n
    q += 1
    n = (int(input('Digite um valor: ')))
print('A quantidade digitada foi de {} valores, e a soma dos mesmos foi de {}'.format(q,s))

