q = 0
p = 0
for i in range (7):
    ano = int(input('Digite o seu ano de nascimento: '))
    if (2021 - ano) < 18:
        q = q + 1
    else:
        p = p + 1
print('A quantidade de pessoas que atingiram a maioridade foi de {}'.format(p))
print('A quantidade de pessoas que não atigiram a maioridade foi de {}'.format(q))

