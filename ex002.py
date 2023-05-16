casa = float(input('Qual o valor do imóvel que você deseja adquirir? R$'))
salario = float(input('Qual o seu salário mensal? R$'))
parcelas = int(input('Em quantas parcelas deseja pagar o empréstimo? '))
vp = casa / parcelas
if vp <= 30/100 * salario:
    print('Parabéns, você conseguiu o empréstimo! As parcelas serão de R${:.2f} pagas em {} vezes'.format(vp,parcelas))
else:
    print('Infelizmente não será possível adquirir o empréstimo!')