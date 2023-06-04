print('-'*20)
print('Tabuada')
print('-'*20)
n = int(input('Digite um número para ver a sua tabuada: '))
print('-'*20)
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
print('-'*20)