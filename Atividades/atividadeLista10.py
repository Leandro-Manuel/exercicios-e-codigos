# Investimento Financeiro

# Desenvolva um programa que simule um investimento financeiro, permitindo que o
# usuario faça projeções sobre o valor do investimento ao longo do tempo.
# O programa deve solicitar ao usuario as seguintes informações:

# O valor inicial do investimento
# A taxa de juros anual (em porcentagem)
# O numero de anos para o investimento

# com base nessas informações, o programa calculará e exibirá o valor do investimento
# ao final de cada ano. O usuario poderá fazer multiplas simulações de investimento
# até que decida encerrar o programa


continuar = True

while (continuar):
    valor_inicial = float(input('Informe o valor inicial do investimento: '))
    valor_taxa = float(input('Insira a taxa de juros anual em porcentagem: '))
    numero_anos = int(input('Informe o número de anos para o investimento: '))
    taxa_juros = valor_taxa / 100

    valor_investimento_ano = valor_inicial


    for _ in range(numero_anos):
        valor_investimento_ano *= ( 1 + taxa_juros)

    print(f'O valor inicial foi {valor_inicial}, a taxa de juros por ano foi {taxa_juros} %')
    print(f'O número de anos do investimento foi {numero_anos}, o valor do investimento final foi {valor_investimento_ano:.2f}')

    continuar = input('Informe se deseja realizar a operação novamente(S/N): ')
    if continuar != 'S':
        continuar = False









