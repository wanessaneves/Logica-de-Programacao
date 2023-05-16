n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O maior valor é primeiro: {}'.format(n1))
elif n1 == n2:
    print('Os valores são iguais: {}'.format(n1))
else:
    print('O maior valor é o segundo: {}'.format(n2))

