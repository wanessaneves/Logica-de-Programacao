def fatorial(num=1, show=bool):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c} x ', end=' ')
        f *= c
    return f



print(fatorial(10,False))




