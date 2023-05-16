from time import sleep


def contador():
    print('~'*25)
    for c in range(1,11):
        sleep(1)
        print(f'{c}')
    print('~'*25)
    for c in range(10,0,-2):
        sleep(1)
        print(f'{c} ')
    i = int(input(' Digite o começo: '))
    f = int(input(' Digite o final da contagem: '))
    p = int(input(' Digite os passos: '))
    print('~'*25)
    for c in range(i,f,p):
        sleep(1)
        print(f'{c}', end=' ')

contador()


