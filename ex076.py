lista = []
par = []
impar = []

while True:
    lista.append(int(input('Digite um valor: ')))
    perg = input('Quer continuar? [S/N]').upper().strip()[0]
    while perg not in 'SsNn':
        print('Digitação inválida, tente novamente!')
        perg = input('Quer continuar? [S/N]').upper().strip()[0]
    if perg in 'Nn':
        break
for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
lista.sort()
par.sort()
impar.sort()

print(f'A lista completa contém os elementos em ordem crescente: {lista}')
print(f'Lista com números pares em ordem crescente: {par}')
print(f'Lista com números ímpares em ordem crescente: {impar}')

