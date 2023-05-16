maior = 0
menor = 0
for c in range(5):
    peso = float(input('Qual o seu peso? '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso


print(maior, menor)
