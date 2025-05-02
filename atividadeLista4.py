# cálculo do consumo médio de combustível

# uma empresa de transporte precisa calcular o consumo médio de combustivel
# de seus veiculos para analisar o desempenho da frota.

# você deve criar um programa que:
# solicite ao usuario a distancia total percorrida (em km) e a quantidade
# de combustivel gasto (em litros).

# calcule o consumo médio, que é a divisão da distancia pelo combustivel
# exiba a classificação do consumo com base na seguinte tabela.

# consumo médio (em km/l)  / classificacao
# menor que 4                  muito ruim
# entre 4 e 8                  ruim
# entre 8.1 e 12               regular
# entre 12.1 e 14              bom
# acima de 14                  excelente


distancia_total = float(input('Insira a distância total percorrida(km): '))
combustivel_gasto = float(input('Informe a quantidade de combustivel gasto na viagem(Litros): '))

consumo_medio = distancia_total / combustivel_gasto


if consumo_medio < 4:
    classificacao = 'muito ruim'

elif consumo_medio >= 4 and consumo_medio<= 8:
    classificacao = 'ruim'

elif consumo_medio >= 8.1 and consumo_medio<= 12:
    classificacao = 'regular'

elif consumo_medio >= 12.1 and consumo_medio<= 14:
    classificacao = 'bom'

else:
    classificacao = 'excelente'

print(f'O consumo médio de combustivel foi {consumo_medio:.2f} km por litro e a classificação foi {classificacao}.')