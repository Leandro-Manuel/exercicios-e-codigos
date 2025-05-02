# controle de produção diaria
# uma fabrica de garrafas plasticas deseja monitorar a produção diaria. cada
# operador da maquina registra, no final do dia, quantas garrafas foram produzidas

# voce deve criar um programa que:

# Solicite ao usuario o numero de dias que deseja registrar.
# para cada dia, solicite a quantidade de garrafas produzidas.

# ao final, exiba: o total de garrafas produzidas, a media de produção por dia
# e uma mensagem de desempenho:

# produção baixa - se a média for menor que 1000 garrafas por dia.
# produção satisfatoria - se estiver entre 1000 e 2000 garrafas por dia
# produção excelente - se for acima de 2000 garrafas por dia.


qtd_dias = int(input('Informe a quantidade de dias que deseja registrar: '))
producao_total = 0
classificacao = None

for x in range(qtd_dias):
    producao_dia = int(input('Informe a quantidade de garrafas produzidas no dia: '))
    producao_total += producao_dia

media_producao = producao_total / qtd_dias

if (media_producao < 1000):
    classificacao = 'Produção Baixa'
elif (media_producao >= 1000 and media_producao <= 2000):
    classificacao = 'Produção Satisfatória'
else:
    classificacao = 'Produção Excelente'

print(f'O total de garrafas produzidas no período de {qtd_dias} dias, foram {producao_total} garrafas.')
print(f'A média de produção por dia foi {media_producao}, e sua classificação foi {classificacao}.')

