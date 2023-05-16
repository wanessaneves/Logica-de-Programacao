aluno = dict()
aluno['nome'] = input('Nome:')
aluno['media'] = float(input(f'Media do aluno(a) {aluno["nome"]}:'))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado!'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado!'

print(aluno)

for k, v in aluno.items():
    print(f'{k} é igual {v}')