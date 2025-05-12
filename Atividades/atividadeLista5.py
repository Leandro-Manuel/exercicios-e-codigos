# Programa de Pontuação por Atividade Física

# Um aplicativo de vida saudável está incentivando as pessoas a se exercitarem
# mais, oferecendo pontos que podem ser trocados por dinheiro em lojas parceiras.
# O sistema de pontuação é baseado no número de horas de atividade física
# realizadas no mês. Veja como funciona:

# até 10 horas de atividade no mês: ganha-se 2 pontos por hora
# de 10 a 20 horas de atividade no mês: ganha-se 5 pontos por hora
# mais de 20 horas de atividade no mês: ganha-se 10 pontos por hora

# escreva um programa que solicite ao usuario quantas horas de atividade
# fisica ele teve no mês, e em seguida, calcule e exiba quantos pontos ele teve.


quantidade_horas_mes = int(input('Qual é a sua quantidade total de horas de atividade física por mês? '))

if quantidade_horas_mes <= 10:
    pontos_totais = quantidade_horas_mes * 2

elif quantidade_horas_mes > 10 and quantidade_horas_mes <= 20:
    pontos_totais = quantidade_horas_mes * 5

else:
    pontos_totais = quantidade_horas_mes * 10

print(f'Você gastou {quantidade_horas_mes} horas de atividade fisica e obteve {pontos_totais} pontos.')