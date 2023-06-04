print('---'*25)
print('Programa para fazer uma tabuada com condição de parada, digite um número negativo para sair.')
print('---'*25)
while True:
    print('---'*25)
    n = int(input('Você quer ver a tabuada de qual número?'))
    if n < 0:
        break
    print('---'*25)
    for m in range(1, 11):
        mult = m * n
        print(f'{m} x {n} = {mult}')
print('A tabuada será encerrada. Obrigado.')
