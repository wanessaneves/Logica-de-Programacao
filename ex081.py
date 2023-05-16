matriz = [[],[],[]]

for c in range (0,9):
    num = int(input('Digite um valor: '))
    if c <= 2:
        matriz[0].append(num)
    elif c <= 5:
        matriz[1].append(num)
    else:
        matriz[2].append(num)
print(f'{matriz[0]}')
print(f'{matriz[1]}')
print(f'{matriz[2]}')
