valor = float(input('Digite o valor do produto: R$'))
condicao = input('Qual será a forma de pagamento? selecione o item correspondente: \n a para cheque/dinheiro; \n b para débito; \n c para crédito').upper().strip()
if condicao == 'A':
    print('O valor a ser pago será de R${:.2f}'.format(valor - (10/100 *valor)))
elif condicao == 'B':
    print('O valor a ser pago será de R${:.2f}'.format(valor - (5/100 * valor)))
elif condicao == 'C':
    d = int(input('Em quantas vezes você quer dividir? '))
    if d <= 2:
        print('O valor a ser pago será de R${:.2f}'.format(valor))
    else:
        print('O valor a ser pago será de R${:.2f}'.format(valor + (20/100 * valor)))
else:
    print('Opção inválida, digite novamente a condição de pagamento desejada!')

