def dimensoes(*matriz):
    cont = 0
    for c in matriz[0]:
            cont += 1
    print(f'{len(matriz)} x {cont}')


print(dimensoes([2,3,4,5,6,8], [6,2,4,8,9,9], [9,5,2,3,4,3], [2,4,9,5,2,5]))
