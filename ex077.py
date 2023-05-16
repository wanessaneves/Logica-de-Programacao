expre = str(input('Digite uma expressão matemática: '))
pilha= []
for simb in expre:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Sua expessão está correta!')
else:
    print('Sua expressão está errada, corrija os parênteses!')

