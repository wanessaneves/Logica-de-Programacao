num = (int(input('Digite um valor: ')),
int(input('Digite outro valor: ')),
int(input('Digite mais um valor: ')),
int(input('Digite o último valor: ')))

print(num)
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)}º posição')
else:
    print('O valor 3 não foi digitado nenhuma vez!')
for n in num:
    if n % 2 == 0:
        m = n
print(f'Os valor pares digitados foram: {m}', end=' ')
