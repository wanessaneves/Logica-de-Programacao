num = []
maior = 0
menor = 0

for c in range(0,5):
    num.append(int(input(f'Digite um valor para a posição {c}°: ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]

print(f'O maior valor foi {maior} nas posições :',end='' )
for i, v in enumerate(num):
    if v == maior:
        print(f'{i} ..')
print(f'e o menor foi {menor} nas posições: ',end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i} ..', end='')