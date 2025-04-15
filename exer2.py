#Desenvolva um programa que faça um cálculo de desconto em uma compra

valor_produto = int(input('Informe o valor do produto em reais: '))

porcentagem_desconto = int(input('Informe a quantidade do desconto do produto(%): '))

valor_desconto = (porcentagem_desconto / 100) * valor_produto

valor_final = valor_produto - valor_desconto

print('O valor do produto após o desconto está em: ',valor_final)
