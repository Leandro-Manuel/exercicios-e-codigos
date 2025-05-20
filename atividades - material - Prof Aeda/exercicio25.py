# Um gerente de farmacia deseja automatizar o calculo do desconto a ser aplicado
# nas vendas de determinados produtos, de acordo com o valor total da compra.
# Escreva um programa que solicite ao usuario que insira o valor total da compra.
# em seguida, o programa deve verificar se o valor total da compra ultrapassa 100 reais.
# se ultrapassar, o programa deve aplicar um desconto de 10% sobre o valor total da compra
# Caso contrário, nenhum desconto será aplicado. O programa deve repetir esse processo
# até que o usuario decida encerrar o programa. Após cada calculo, o programa deve exibir
# o valor total da compra com desconto, se aplicavel, e perguntar ao usuario se deseja
# realizar outra compra.

opcao = 'S'
valorFinal = 0
while(opcao in 'Ss'):
    valorTotalCompra = float(input('insira o valor total da compra: '))
    if valorTotalCompra > 100:
        valorFinal = valorTotalCompra - (valorTotalCompra * 0.1)
        print(f'O valor final com desconto de 10% foi {valorFinal} reais.')
    else:
        print('Nenhum desconto aplicado.')
    opcao = input('Deseja realizar novamente?(S/N): ')
