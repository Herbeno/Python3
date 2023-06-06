# Algoritmo para criar uma tabuada utilizando a estrutura de repetição 'for'.
print('-'*20)
print('Tabuada')
print('-'*20)
n = int(input('Digite um número para ver a sua tabuada: '))
print('-'*20)
# Ao usar o 'for' o primerio número entre parenteses é o número de início da repetição.
# Um detalhe para ficar atento é que o segundo número que está entre parenteses não é o último da repetição, e sim o último+1, ou seja, em uma repetição de x até y, o comando 'for' ficará da seguinte forma 'for c in range(x,Y+1):' sendo 'c' o contador.
for c in range(1, 11):
    print('{} x {} = {}'.format(n, c, n*c))
print('-'*20)
