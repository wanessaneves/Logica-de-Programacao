matriz = [[],[],[]]
somapar = 0
somater = 0

for c in range (0,9):
    num = int(input('Digite um valor: '))
    if c <= 2:
        matriz[0].append(num)
    elif c <= 5:
        matriz[1].append(num)
    else:
        matriz[2].append(num)
    if num % 2 == 0:
        somapar += num
for e in matriz:
    somater += e[2]

print(matriz[0])
print(matriz[1])
print(matriz[2])
print(f'A soma dos números pares digitados é: {somapar}')
print(f'A soma de todos os valores digitados na terceira coluna é {somater}')