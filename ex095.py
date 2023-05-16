def voto(num):
    ano = 2021 - num
    if ano < 18:
        print(f'VOTO NEGADO! Pois sua idade é de {ano} anos. ')
    elif 18 <= ano < 60:
        print(f'VOTO OBRIGATÓRIO! Pois sua idade é de {ano} anos. ')
    else:
        print(f'VOTO OPCIONAL! Pois sua idade é de {ano} anos .')

idade = voto(int(input(f'Qual o ano do seu nascimento?')))