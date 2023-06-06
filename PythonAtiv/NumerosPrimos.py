# Neste código, veremos um algoritmo em que pede-se um número e ele analisará se o número é primo ou não, utilizando o 'for'.
n = int(input('Digite um número inteiro para saber se ele é número primo: '))
tot = 0
# Para fazer isto, usaremos uma estrutura de repetição 'for'.
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
    