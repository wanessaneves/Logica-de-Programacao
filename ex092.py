from time import sleep
def maior(* num):
    cont = mai = 0
    print('~' * 30)
    print('Analisando os valores....')
    print('~'*30)
    for v in num:
        print(f'{v}', end=' ', flush=True)
        sleep(1)
        if cont == 0:
            mai = v
        else:
            if v > mai:
                mai = v
        cont += 1
    print(f'Foram informados {cont} valores.')
    sleep(1)
    print(f'O maior valor dentre eles foi {mai}')
    sleep(1)



maior(2,5,6,8,9,10,25)
maior(5,6,12,15,42)
maior(65,23,105,24,96)
