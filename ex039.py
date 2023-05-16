ano = int(input('Qual o ano do seu nascimento? '))
data = 2021 - ano
if data <= 9:
    print('ALUNO(A) MIRIM')
elif data <= 14:
    print('ALUNO(A) INFANTIL')
elif data <= 19:
    print('ALUNO(A) JUNIOR')
elif data == 20:
    print('ALUNO(A) SENIOR')
else:
    print('ALUNO(A) MASTER')
