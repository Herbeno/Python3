# Nesta atividade, faremos um algoritmo simples que leia a temperatura que será indicada em Cº e tranforme para Fº e mostre este valor correspondente.
c = float(input('Qual a temperatura em Cº?'))
# Sabemos que para converter de celsios para fahrenheit temos que usar a seguinte fórmula: F = (C * 9/5) + 32
print(f'Esta temperatura em Fº corresponde a {(c*(9/5)) + 32}')
