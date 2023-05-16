# Ordem de precedencia para cálculo:
# parenteses ()
# potencia **; divisão /, multiplicação *, resto da divisão % e divisão inteira //
# soma + e subtração.

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, a divisão é {:.2f}, a divisão inteira é {}, e a exponenciação é {}'.format(s,m,d,di,e))








