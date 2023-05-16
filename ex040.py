l1 = float(input('Digite o primeiro lado do triângulo: '))
l2 = float(input('Digite o segundo lado do triângulo: '))
l3 = float(input('Digite o terceiro lado do triângulo: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 != l2 and l2 != l3 and l1 != l3:
        print('É um triângulo escaleno pois possui ambos os lados diferentes!')
    elif l1 == l2 and l1 == l3:
        print('É um triângulo equilátero, todos os lados são iguais!')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('É um triângulo isósceles, possui dois lados iguais!')
else:
    print('Os valor digitados não correspondem a um triângulo!')

