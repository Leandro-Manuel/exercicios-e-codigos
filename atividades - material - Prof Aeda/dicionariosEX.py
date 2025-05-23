# Você foi designado para criar um programa para armazenar uma lista de produtos
# em um estoque. O programa deve solicitar ao usuario que insira o nome(chave) e a
# quantidade de cada produto, e etnão armazenar esses produtos em uma lista de
# dicionarios. o usuario pode continuar adicionando produtos ao estoque até decidir
# sair do programa.

estoque_produtos = {}

while True:
    nome_produto = input('Insira o nome do produto: ')
    qtd_produto = int(input('Insira a quantidade do produto: '))

    estoque_produtos[nome_produto] = qtd_produto
    opcao = input('Deseja continuar? (S/N): ')
    if opcao != 'S':
        print('Encerrando o programa...')
        break
print(estoque_produtos)

estoque = []
while True:
    nome = input('Digite o nome do produto (ou "sair" para encerrar): ')
    if nome.lower() == 'sair':
        break

    quantidade = int(input('Digite a quantidade do produto: '))

    produto = {'nome': nome, 'quantidade': quantidade}
    estoque.append(produto)

print('\nProdutos no estoque: ')
for produto in estoque:
    print(f'Nome: {produto['nome']}, quantidade: {produto['quantidade']}')


