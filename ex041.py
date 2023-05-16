peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite sua altura em Metros: '))
imc = peso/(altura**2)
print('O seu índice de massa corpórea é de {:.2f}'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso!')
elif 18.5 < imc <= 25:
    print('Você está no peso ideal!')
elif 25 < imc <= 30:
    print('Você está com sobrepeso!')
elif 30 < imc <= 40:
    print('Você é considerado obeso(a)!')
else:
    print('Você está com obesidade mórbida!')


