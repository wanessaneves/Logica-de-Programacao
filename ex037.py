data = int(input('Digite o ano do seu nascimento: '))
ano = 2021 - data
if ano < 18:
    print('Você ainda vai estar apto para se alistar, faltam {} anos.'.format(18-ano))
elif ano == 18:
    print('Parabéns, você já pode se alistar!')
else:
    print('Você ultrapassou o prazo de alistamento em {} anos!'.format(ano - 18))
