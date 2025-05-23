# Um distribuidor de refrigerantes vende seu produto em todo o pais
# em cada trimestre do ano passado, ele vendeu uma certa quantidade de garrafas em cada
# regiao do brasil. Faça um algoritmo para ler as quantidades vendidas e escrever
# a quantidade total vendida em todo o pais.


matriz = [
    [], [], [], []
]
soma = 0
for t in range(4):
    for r in range(5):
        matriz[t].append(float(input(f'insira a quantidade de vendas do semestre {t+1} da região {r+1}: ')))
        soma += matriz[t][r]
print(f'O total de vendas é: {soma}')

vendas_por_ano = [
    [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
]

regiao = ['Norte','Nordeste','Sul','Sudeste','Centro-Oeste']
trimestre = ['1 - Trimestre:', '2 - Trimestre','3 - Trimestre','4 - Trimestre']

for x in range(5):
    for y in range(4):
        vendas_por_ano[x][y] = float(input(f'Insira o valor da venda do {trimestre[y]} , da região {regiao[x]}: '))

print(vendas_por_ano)
