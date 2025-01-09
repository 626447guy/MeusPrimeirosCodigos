cont = 0
n = int(input('Digite um valor'))
if n > 1:
    for i in range(1, 11):
        if n % i == 0:
            cont +=1
    if cont > 2:
      print (f'Não é primo. Ele é divisível {cont} vezes')
    else:
       print(f'É primo. ele é divisível apenas {cont} vezes')
else:
       print(f'Não é divisível') 