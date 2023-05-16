total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    valor = float(input('Preço do produto: R$ '))
    cont +=1
    total += valor
    if valor > 1000:
        totmil += 1
    if cont == 1:
        menor = valor
        barato = produto
    else:
        if valor < menor:
            menor = valor
            barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break
print('Fim do programa!')
print(f'O valor total da compra foi de R${total}')
print(f'O total de produtos com o valor maior que R$1000,00 foi de {totmil}')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')