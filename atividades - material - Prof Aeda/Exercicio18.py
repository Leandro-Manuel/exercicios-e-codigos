# Foi conduzida uma pesquisa com 10 mulheres para determinar o numero de filhos
# que elas tem. Escreva um programa para analisar os resultados da pesquisa e contar
# quantas dessas mulheres possuem até 2 filhos e quantas possuem mais de 2 filhos.

# o programa deve solicitar ao usuario que insira o numero de filhos de cada uma
# das 10 mulheres e, em seguida, calcular e exibir o total de mulheres que possuem
# até 2 filhos e o total de mulheres que possuem mais de 2 filhos.

contador = 1
ate_2 = mais_2 = 0
while (contador <= 10):
    qtd_filhos = int(input(f'Quantos filhos a {contador} mulher tem? '))
    if qtd_filhos <= 2:
        ate_2 += 1
    else:
        mais_2 += 1
    contador += 1
print(f'O total de mulheres que possuem até 2 filhos são {ate_2} mulheres.')
print(f'O total de mulheres que possuem mais de 2 filhos são {mais_2} mulheres.')
