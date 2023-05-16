dados = {}
idade = 0
dados['Nome'] = input('Nome: ')
ano = int(input('Ano de nascimento: '))
if ano != 0:
    idade = 2021 - ano
dados['Idade'] = idade
dados ['ctps'] = int(input('Carteira de trabalho: [Digite 0 se não tiver!] '))
if dados['ctps'] != 0 :
    dados['contratação'] = int(input('Digite o ano de contratação: '))
    dados ['salário'] = float(input('Digite o seu salário atual: '))
temp = 2021 - dados['contratação']
aposent = 32 - temp
aposentadoria = idade + aposent
for k, v in dados.items():
    print(f'{k} possui valor {v}')
print(f'Você vai se aposentar com {aposentadoria} anos!')