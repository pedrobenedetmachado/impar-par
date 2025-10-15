from random import randint
v = 0
while True:
    print('-=' * 20)
    print('VAMOS JOGAR IMPER PAR!')
    print('-=' * 20)
    j = int(input('Digite um valor: '))
    c = randint(0, 11)
    total = j + c
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('par ou impar? [P/I]: ')).strip().upper()[0]
    print(f'você jogou {j} e o computador jogou {c} e o total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('você venceu!')
            v += 1
        else:
            print('você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('você venceu!')
            v += 1
        else:
            print('você perdeu!')
            break
    print('vamos jogar novamente...')
print(f'GAME OVER! você venceu {v} vezes.')
