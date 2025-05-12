# crie um algoritmo que peça o valor do produto e a porcentagem do desconto. calcule o valor final aplicando o desconto.
# imprima o valor final com desconto.

valor_produto = float(input('Informe o valor do produto: '))
porcentagem = float(input('Informe a porcentagem de desconto do produto: '))

valor_desconto = valor_produto * (porcentagem/100)

valor_final = valor_produto - valor_desconto

print(f'O valor do produto com desconto é {valor_final}')