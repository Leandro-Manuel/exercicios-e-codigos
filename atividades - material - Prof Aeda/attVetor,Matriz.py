# Uma vendedora deseja analisar seu desempenho de vendas diárias.
# Desenvolva um programa que:

# solicite ao usuario a quantidade de produtos vendidos no dia.
# crie um vetor para armazenar o peso de cada produto vendido,
# onde o usuario insere o peso de cada produto.
# identifique e exiba o maior e o menor peso vendidos. considere que cada quilograma(kg)
# de produto vendido custa 4.35 reais e imprima o valor total arrecadado no dia.

qtd_produtos = int(input('Insira a quantidade de produtos vendidos no dia: '))

nome_produto = []
peso_produto = []



for x in range(qtd_produtos):
    peso = float(input('Insira o peso do produto: '))
    peso_produto.append(peso)

total_arrecadado =  sum(peso_produto) * 4.35
peso_medio = sum(peso_produto) / len(peso_produto)
menor_peso = min(peso_produto)
maior_peso = max(peso_produto)

print(f'O peso médio das vendas: {peso_medio:.2f}')
print(f'O maior peso: {maior_peso:.2f}, o menor peso: {menor_peso:.2f}')
print(f'Total arrecadado no dia: {total_arrecadado:.2f} reais.')


