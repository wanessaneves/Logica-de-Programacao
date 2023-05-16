from time import sleep
lista = []
total = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    perg = input('Você quer continuar? [S/N]').upper().strip()[0]
    while perg not in 'SsNn':
        print('Você digitou um valor errado, tente novamente...')
        perg = input('Você quer continuar? [S/N]').upper().strip()[0]
    if perg in 'Nn':
        break
for l in lista:
    total += 1
lista.sort()
lista.sort(reverse=True)
if 5 in lista:
    print('O valor 5 está contido na lista!')
else:
    print('O valor 5 não está contido na lista!')
sleep(2)
print(f'A sua lista contem esses elementos em ordem decrescente: {lista}')
print(f'Foram digitados {total} números!')
