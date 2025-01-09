num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))
action = str(input('Escolha uma ação: Add(a), Subs(s), Mult(m), div(d) -> '))

print('O resultado é:', end=' ')
if action == 'a':
    print(num1 + num2)
elif action == 's':
    print(num1 - num2)
elif action == 'm':
    print(num1 * num2)
elif action == 'd':
    print(num1 / num2)
else:
    print('Ação inválida')