salario = float(input('Qual o seu salário? '))
if salario <= 1250:
    print('Com o reajuste salarial de 15% seu novo salário é de R$ {:.2f}'.format((15/100*salario) + salario))
else:
    print('Com o reajuste salarial de 10% seu novo salário é de R$ {:.2f}'.format((10/100*salario) + salario))
