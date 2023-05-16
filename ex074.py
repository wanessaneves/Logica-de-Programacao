from time import sleep
lista = []

while True:
    l = int(input('Digite um valor: '))
    if l not in lista:
        lista.append(l)
        print('Valor adicionado com sucesso!')
    else:
        print('o valor digitado já existe, digite outro valor!')
    perg = input('Quer continuar? [S/N]').upper().strip()[0]
    while perg not in 'SsNn':
        print('Resposta errada, tente novamente!')
        perg = input('Quer continuar? [S/N]').upper().strip()[0]
    if perg in 'Nn':
        break
lista.sort()
print('Aguarde um momento, estamos ordenando a sua lista!')
sleep(2)
print(f'A sua lista é : {lista}')
