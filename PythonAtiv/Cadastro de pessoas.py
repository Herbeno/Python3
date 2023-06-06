# Nesta atividade, construiremos um algoritmo que leia a idade e sexo(M/F) para fazer cadastro de pessoas e ao final de cada cadastro, perguntará se a pessoa deseja continuar a cadastrar pessoas, se sim, continua, se não ele dará o número total de pessoas com mais de 18 anos, o número total de homens cadastrados e o total de mulheres com menos de 20 anos.
# Para iniciar, criaremos as variáveis de total de pessoas com mais de 18(que chamaremos de tot18), total de homens(totalh) e total de mulheres com menos de 20 anos(totm20)
tot18 = 0
totalh = 0
totm20 = 0
# Para esta atividade, usaremos a estrutura de repetição while true
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totalh += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
# Quando usamos o 'break' a estrutura de repetição irá parar e o algoritmo irá executar o que vem depois dela. Que neste caso será o resultado do que foi pedido no início da atividade.
print(f'Total de pessoas com mais de 18 anos é {tot18}.')
print(f'Total de homens cadastrados é {totalh}.')
print(f'Total de mulheres com menos de 20 anos é {totm20}.')
