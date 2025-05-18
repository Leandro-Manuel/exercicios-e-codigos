# Um estacionamento deseja automatizar o calculo das taxas a serem cobradas
# dos clientes com base no tempo de permanencia de seus veiculos. O programa deve
# solicitar ao usuario a hora de entrada e a hora de saido do veiculo e calcular
# a taxa de estacionamento de acordo com as seguintes regras:

# para permanencia de até 1 hora, a taxa é de 5 reais.
# para cada hora adicional após a primeira, a taxa é de 3 reais por hora.

# alem disso, o sistema deve oferecer descontos especiais para clientes frequentes.
# clientes que utilizam o estacionamento mais de 10 vezes no mes tem direito a um desconto
# de 20% em sua taxa.

hora_entrada = int(input('Insira a hora de entrada: '))
minuto_entrada = int(input('Insira o minuto de entrada: '))
hora_saida = int(input('Insira a hora de saida: '))
minuto_saida = int(input('Insira o minuto de saida: '))
permanencia_minuto = 0

permanencia_hora = hora_saida - hora_entrada

if minuto_entrada >= minuto_saida:
    permanecia_minuto = minuto_entrada - minuto_saida
else:
    permanencia_minuto = minuto_saida - minuto_entrada

if permanencia_hora <= 1:
    taxa = 5
else:
    taxa = 5 + ((permanencia_hora - 1) * 3)

qtd = int(input('Quantas vezes você utilizou o estacionamento este mês? '))
if qtd > 10:
    taxa -= taxa * 0.20


print(f'O tempo total de permanencia no estacinamento foi {permanencia_hora} hora(s) e {permanencia_minuto} minuto(s). Sua taxa: {taxa} reais.')



