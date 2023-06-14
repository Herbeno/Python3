# Nesta atividade faremos um 'Caixa eletrônico que pedirá o valor de quanto deseja sacar em reais, e irá mostrar quantas cédulas de 50, 20 e 10 irão ser sacadas em ordem da maior para a menor. Para isso, usaremos 'while True', 'if', 'elif' e 'else'.
print('---'*15)
print('CAIXA ELETRONICO')
print('---'*15)
valor = int(input('Quanto você deseja sacar? R$' ))
total = valor 
# Iniciaremos com o valor da cédula mais alta, que neste caso é de R$ 50
cedula = 50
# Valor inicial de cédulas será zero
totcedulas = 0
# Agora usaremos a estrutura de repetição 'while True'. Que faz com que o loop se repita enquanto a condição for verdadeira.
while True:
    # Abaixo indicamos que enquanto o total de reais que serão sacados forem maiores ou iguais ao número de cédulas, será subtraído o valor correspondente a cédula do total e será adicionada uma cédula a mais.
    if total >= cedula:
        total -= cedula
        totcedulas += 1
    else:
        # agora indicamos o que acontecer quando o total for menor que o valor da cédula.
        if totcedulas > 0:
            print(f'O total de {totcedulas} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break