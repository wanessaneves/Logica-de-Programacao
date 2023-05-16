while True:
    n = int(input('Digite um valor para verificar a tabuada: '))
    if n < 0:
        break
    for c in range (1,11):
        t = n * c
        print(f'{n} X {c} = {t}')
print('O valor digitado foi negativo! Tabuada encerrada!!')
