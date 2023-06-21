n = int(input('Digite um número para saber seu fatorial: '))
fatorial = 0
soma = 0
c = n
n2 = n * c
while c != 1:
    soma += n2
    print('{}'.format(c), end='x ')
    c -= 1
if c == 1:
    soma += n2
    print('{}'.format(c))
    c -= 1
fatorial = soma
print(f'O fatorial de {n} = {fatorial}.')
