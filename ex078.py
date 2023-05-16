galera = list()
dados = list()
totmai = 0
totmen = 0

for i in range (0,3):
    dados.append(str(input('Digite o seu nome: ')))
    dados.append(int(input('Digite sua idade: ')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade!')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totmen += 1
print(f'No total foram {totmai} pessoas na maioridade e {totmen} menores de idade')