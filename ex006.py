n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m < 5:
    print('REPROVADO(A)!')
elif 5 < m < 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO(A)')
print('Sua média foi de {:.2f}.'.format(m))
