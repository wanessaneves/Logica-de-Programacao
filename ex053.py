sexo = input('Digite seu sexo: \n 1. M para Masculino \n 2. F para Feminino:').strip().upper()
while sexo not in 'MmFf':
    sexo = input('Dados inválidos, digite novamente: \n 1. M para Masculino \n 2. F para Feminino:').strip().upper()
print('Sexo {} registrado com sucesso!'.format(sexo))