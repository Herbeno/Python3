# Nesta atividade teremos que fazer o famoso jogo Jokenpô(pedra, papelo ou tesoura), com o uso do 'if', 'elif' e 'else'.
# Paraisso, precisaremos importar a função 'randint' no módulo 'random'.
from random import randint
# A função sleep serve para realizar uma contagem em algum momento enquanto estiver realizando a leitura do código. Ao passar da quantidade de segundos estabelecida, a leitura do código continua normalmente.
from time import sleep
print('***'*5)
print('    {}JOKENPÔ{}'.format('\033[7m', '\033[m'))
print('***'*5)
lista = ('pedra', 'papel', 'tesoura')
print('''[ 0 ] Pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador = int(input('Escolha pedra, papel ou tesoura: '))
print('JÓ')
sleep(1)
print('Quem')
sleep(1)
print('PÔ')
sleep(1)
# Quando usamos o 'randint', temos que lembrar que sempre o primeiro item da lista corresponde ao número '0' e o último é o último menos um.
escolhapc = randint(0, 2)
print('---'*10)
print('Você escolheu {}'.format(lista[jogador]))
print('O computador escolheu {}'.format(lista[escolhapc]))
print('---'*10)
# Aqui usaremos o 'if', 'elif' e 'else' para definir as condições para o jogo.
if jogador == 0 and escolhapc == 1:
    print('O vencedor foi o computador!')
elif jogador == 1 and escolhapc == 2:
    print('O vencedor foi o computador!')
elif jogador == 2 and escolhapc == 0:
    print('O vencedor foi o computador!')
elif jogador == escolhapc:
    print('O jogo ficou empatado!')
else:
    print('Você venceu! {}parabéns{}!'.format('\033[7m', '\033[m'))
