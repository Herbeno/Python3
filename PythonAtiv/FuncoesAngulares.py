from math import radians, sin, cos, tan
print('**'*40)
print('Digite um ângulo e descubra qual é seu Seno, seu Cosseno e sua Tangente! ')
print('**'*40)
a = int(input('Escolha um ângulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O ângulo escolhido foi {}°'.format(a))
print('-')
print('O Seno deste é {:.2f}'.format(s))
print('-')
print('O Cosseno deste ângulo é {:.2f}'.format(c))
print('-')
print('E a Tangente deste ângulo é {:.2f}'.format(t))
