# Você foi encarregado de desenvolver um simulador de economia de combustivel para uma
# empresa de transporte que opera uma frota de veiculos. Este simulador ajudara a empresa
# a calcular os custos de combustivel para diferentes tipos de veiculos em suas rotas.

# o programa solicitara ao usuario as seguintes informaçoes:

# tipo de veiculo, carro, caminhao, onibus
# distancia a ser percorrida (em quilometros)
# consumo medio de combustivel do veiculo (em quilometros por litro)
# preço médio do combustivel por litro.

# com base nessas informações, o programa calculara e exibira na tela:
# a quantidade total de combustivel necessario para percorrer a distancia fornecida
# o custo total do combustivel necessario, considerando o preço medio fornecido.
# uma comparacao entre o custo total do combustivel e o custo se fosse aplicado
# um desconto de 10% sobre o preço médio do combustivel.

# apos exibir os resultados, o programa perguntara ao usuario se deseja realizar outra
# simulação ou encerrar o programa.

opcao = 'S'
while (opcao in 'Ss'):

    tipo_veiculo = int(input('Informe o tipo de veiculo: 1 - carro, 2 - caminhao, 3 - onibus: '))
    distanciaKm = int(input('Informe a distancia a ser percorrida(km): '))
    consumo_litro = float(input('Insira o consumo médio de combustivel do veiculo (km por litro): '))
    preco_medio_litro = float(input('Insira o preço médio do combustível por litro: '))

    qtdTotal_combustivel = distanciaKm / consumo_litro
    custo_combustivel = qtdTotal_combustivel * preco_medio_litro
    custoComDesconto = custo_combustivel - (custo_combustivel * 0.1)

    print(f'A quantidade total de combustível necessário para percorrer a distancia de '
          f'{distanciaKm} km é {qtdTotal_combustivel:.2f} litros.')
    print(f'O custo total do combustivel seria de {custo_combustivel:.2f} reais.')
    print(f'Caso houvesse um desconto de 10% no custo total, o valor seria de {custoComDesconto:.2f} reais.')

    opcao = input('Deseja realizar a operação novamente?(S/N): ')




