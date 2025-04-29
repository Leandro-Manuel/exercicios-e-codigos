# Organização de Evento Escolar

#A professora Joana está organizando uma feira de ciencias na escola.
# Para isso, ela e outros 5 professores vão dividir os custos igualmente.
# eles vão comprar camisetas personalizadas, cartolinas e canetas coloridas
# para a decoração. Escreva um programa que receba como entrada o valor
# das camisetas, a quantidade e o valor unitario de cada material (cartolina
# e canetas), calcule e exiba o valor total e o valor a ser pago por cada prof

# entradas esperadas: valor das camisetas, quantidade de cartolinas e valor
#unitario, quantidade de canetas e valor unitario

#saida esperada: total gasto, valor por professor

valor_camisetas = float(input('Insira o valor total das camisetas: '))

quantidade_cartolinas = float(input('Insira a quantidade de cartilas a comprar: '))
valor_cartolina = float(input('Informe o valor unitário da cartolina: '))

quantidade_canetas = float(input('Insira a quantidade de canetas a comprar: '))
valor_caneta = float(input('Informe o valor unitário da caneta: '))

valor_total_gasto = valor_camisetas + (quantidade_cartolinas * valor_cartolina) + (quantidade_canetas * valor_caneta)
valor_total_por_professor = valor_total_gasto / 6

print(f'O valor total gasto foi {valor_total_gasto} reais. Cada professor deverá pagar {valor_total_por_professor:.2f} reais.')




