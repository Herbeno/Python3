n = int(input('Digite um número inteiro para saber se ele é número primo: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
    else:
        tot += 0
print('\033[4;34mO Número {} é divisível {} vezes.'.format(n, tot))
if tot == 2:
    print('O número {} é um número primo.'.format(n))
else:
    print('O número {} não é um número primo.'.format(n))
    