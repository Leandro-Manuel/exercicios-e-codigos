# Uma loja de peças de carro deseja implementar um sistema automatizado para que os
# clientes possam fazer pedidos de forma mais conveniente. O catalogo da loja é composto
# por uma variedade de peças, cada uma com um codigo unico, um nome e um preço
# correspondente, conforme descrito na tabela abaixo:

# codigo  /  item  / preço
# 1        bateria    200
# 2        Pneu       350
# 3   Filtro de óleo  20
# 4   Pastilhas de Freio 100

# O sistema deve permitir que os clientes façam seus pedidos selecionando o numero
# correspondente ao codigo do item desejado. Após a escolha do item, o sistema deve
# calcular o valor total do pedido.

def menu():
    print('código - produto - Preço')
    print('  1  -  Bateria  -  200')
    print('  2  -    Pneu  -  350')
    print('  3  -  Filtro de óleo  -  20')
    print('  4  -  Pastilhas de freio  -  100')

exibir_menu = menu()

escolha = int(input('Escolha o produto com o código: '))
qtd = int(input('Selecione a quantidade: '))

match (escolha):
    case 1:
        valor = 200 * qtd
    case 2:
        valor = 350 * qtd
    case 3:
        valor = 20 * qtd
    case 4:
        valor = 100 * qtd
    case _:
        print('Opção inválida, tente novamente.')
print(f'O valor total da sua compra foi {valor} reais.')
