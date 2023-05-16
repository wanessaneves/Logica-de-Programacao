s = float(input('Digite o seu salário mensal para saber o novo valor a partir do reajuste de 15%: R$'))
r = s * (15/100)
ns = s + r
print('O seu novo salário é de R$ {:.2f}'.format(ns))



