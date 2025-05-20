# Uma revendedora de carros oferece aos seus vendedores um salário mensal fixo,
# além de uma comissão fixa pelos carros vendido e 5% do valor total das vendas
# efetuadas por eles. Escreva um programa em Python que leia o numero de carros
# por ele vendidos, o valor total de suas vendas, o salario fixo e a comissão
# que ele recebe por carro vendido. Calcule e escreva o salario final do vendedor.

salario_fixo = float(input('Insira o seu salário fixo mensal: '))
carros_vendidos = int(input('Informe a quantidade de carros vendidos: '))
total_vendas = int(input('Insira o valor total das vendas: '))
comissao = (float(input('Insira a comissão por venda: ')))

salario_final = salario_fixo + (carros_vendidos * comissao) + (total_vendas * 0.05)

print(f'O seu salário final foi {salario_final:.2f} reais.')
