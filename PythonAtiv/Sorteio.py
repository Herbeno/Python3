# Esta atividade visa criar um algoritmo que faça um sorteio entre 4 alunos para ver qual deles foi o sorteado para apagar o quadro.
print('-'*25)
print('Soretio entre 4 alunos.')
print('-'*25)
# O comando abaixo serve para importar a função 'choice', que retorna um item aleatório da lista dada. 
from random import choice
a = str(input('Nome do primeiro aluno: '))
b = str(input('Nome do segundo aluno: '))
c = str(input('Nome do terceiro aluno: '))
d = str(input('Nome do quarto aluno: '))
# No próximo comando, criaremos a lista na qual iremos usar a função 'choice'.
lista = [a, b, c, d]
escolhido = choice(lista)
print('-'*45)
print('O aluno escolhido pelo sorteio foi {}'.format(escolhido))
print('-'*45)
