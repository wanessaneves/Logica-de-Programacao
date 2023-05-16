num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] Converter para binário
[2] Converter para hexadecimal 
[3] Converter para octal''')
opcao = int(input('Sua opção é? '))
if opcao == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
elif opcao == 3:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
else:
    print('Opção inválida, tente novamente!')
