secreto = 'abacaxi'
digitadas = []
chances = 5 
print('+-' * 20)
print('JOGO DA FORCA PYTHON - MADE BY: BRUNA')
print('-=' * 20)

while True:
    print(f'A palavra secreta está assim: {"".join([letra if letra in digitadas else "*" for letra in secreto])}')
    
    if "".join([letra if letra in digitadas else "*" for letra in secreto]) == secreto:
        print('VOCÊ VENCEU E ESCAPOU DA FORCA!')
        break

    letra = str(input('Digite uma letra:')).lower()  # Força a entrada para minúsculas

    if len(letra) > 1:
        print('ERRO, não vale digitar mais de uma letra.')
        continue

    if letra in digitadas:
        print('Você já digitou essa letra. Tente outra.')
        continue
    
    digitadas.append(letra)

    if letra not in secreto:
        chances -= 1
        print(f'A letra "{letra}" não está na palavra secreta.')
        if chances <= 0:
            print('VOCÊ PERDEU!! FORCA!!')
            break
    else:
        print(f'A letra "{letra}" está na palavra secreta.')

    print(f'Você tem {chances} chances.')

    print('\n')  # Usado para espaçar as rodadas