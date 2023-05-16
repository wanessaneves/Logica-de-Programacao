lista = []
alunos = []
media = []
while True:
    alunos.append(input('Digite o nome do aluno: '))
    alunos.append(float(input('Digite a primeira nota: ')))
    alunos.append(float(input('Digite a segunda nota: ')))
    lista.append(alunos[:])
    alunos.clear()
    perg = input('Quer continuar? [S/N]: ')
    while perg not in 'SsNn':
        print('Digitação inválida, tente novamente!')
        perg = input('Quer continuar? [S/N]: ')
    if perg in 'Nn':
        break
for i in lista:
    media.append((i[1] + i[2])/2)
print(f'A média do aluno(a) {lista[0]}foi {media})
print(lista)

