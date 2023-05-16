s = q = n = 0

while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
    q += 1
print(f'A quantidade digitada foi de {q} e a soma dos números resultou em {s}')