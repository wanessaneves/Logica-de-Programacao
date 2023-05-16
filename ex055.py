from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
menu = 0

while menu != 5:
    menu = int(input('''O que você deseja fazer?
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MOSTRAR O MAIOR VALOR
    [4] DIGITAR NOVOS VALORES
    [5] SAIR DO PROGRAMA'''))
    if menu == 1:
        print('A soma dos valores {} e {} é {}'. format(n1, n2, (n1+n2)))
    elif menu == 2:
        print('A multiplicação dos valores {} e {} é {}'.format(n1, n2, (n1*n2)))
    elif menu == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior valor entre {} e {} é {}'.format(n1, n2, maior))
    elif menu == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif menu == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida, tente novamente!')
print('FIM DO PROGRAMA!')