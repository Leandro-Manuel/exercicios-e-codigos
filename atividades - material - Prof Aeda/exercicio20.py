# Você foi designado para desenvolver uma calculadora de descontos para uma loja de
# roupas. O programa deve solicitar ao usuario o valor total da compra e a quantidade
# de itens adquiridos. Em seguida, baseado na quantidade de itens comprados, o programa
# deve aplicar descontos progressivos da seguinte forma:

# para compras de até 5 itens: sem desconto
# para compras de 6 a 10 itens: desconto de 5% sobre o valor total.
# para compras de mais de 10 itens: desconto de 10% sobre o valor total.

# apos aplicar o desconto correspondente, o programa deve exibir na tela o valor
# total da compra com o desconto aplicado. Além disso, o usuario deve ter a opção
# de realizar o calculo novamente ou encerrar o programa.

opcao = 'S'
while (opcao in 'Ss'):
    valor_total = float(input('Insira o valor total da sua compra: '))
    qtd_itens = int(input('Insira a quantidade de itens adquiridos: '))
    valor_desconto = 0

    if qtd_itens > 10:
        valor_desconto = valor_total - (valor_total * 0.1)
    elif qtd_itens >= 6 and qtd_itens <= 10:
        valor_desconto = valor_total - (valor_total * 0.05)
    else:
        print('Não há desconto')
    print(f'O valor a ser pago é de {valor_desconto} reais.')

    opcao = input('Deseja realizar o calculo novamente?(S/N): ')




