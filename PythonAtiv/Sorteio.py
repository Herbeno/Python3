print('-'*25)
print('Soretio entre 4 alunos.')
print('-'*25)
from random import choice
a = str(input('Nome do primeiro aluno: '))
b = str(input('Nome do segundo aluno: '))
c = str(input('Nome do terceiro aluno: '))
d = str(input('Nome do quarto aluno: '))
lista = [a, b, c, d]
escolhido = choice(lista)
print('-'*45)
print('O aluno escolhido pelo sorteio foi {}'.format(escolhido))
print('-'*45)
