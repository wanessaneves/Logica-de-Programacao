print('Olá consumidor, neste dia a loja estará com 10% de desconto em todos os produtos, coloque o valor da mercadoria abaixo e aproveite!')
vo = float(input('Digite o valor da mercadoria: R$  '))
d = vo * (10/100)
vf = vo - d
print('Caro cliente, aplicando o desconto de 10% o novo valor da sua mercadoria é de R$ {:.2f}'.format(vf))
