num =[[],[]]

for c in range(0,7):
    n = (int(input('Digite um valor: ')))
    if n % 2 == 0:
        num[0].append(n)
        num[0].sort()
    else:
        num[1].append(n)
        num[1].sort()
print(num)