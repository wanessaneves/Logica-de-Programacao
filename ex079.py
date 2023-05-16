lista = []
outlist = []
pessoas = 0
maior = menor = 0

while True:
    outlist.append(str(input('Digite um nome: ')))
    outlist.append(float(input('Digite o peso: ')))
    if len(lista) == 0:
        maior = menor = outlist[1]
    else:
        if outlist[1] > maior:
            maior = outlist[1]
        if outlist[1] < menor:
            menor = outlist[1]
    lista.append(outlist[:])
    outlist.clear()
    perg = input('Deseja continuar? [S/N]')
    while perg not in 'SsNn':
        print('Opção inválida, digite novamente!')
        perg = input('Deseja continuar? [S/N]')
    if perg in 'Nn':
        break

for p in lista:
    pessoas += 1
    if p[1] == maior:
        print(f'A pessoa com o maior peso foi {p[0]} com {maior} kg')
    if p[1] == menor:
        print(f'A pessoa com o menor peso foi {p[0]} com {menor} kg')
print(f'Foram cadastradas ao todo {pessoas} pessoas')