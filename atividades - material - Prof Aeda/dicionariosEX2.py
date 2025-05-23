# Você trabalha em uma empresa de seguros de automoveis. Sua tarefa é criar um programa
# que colete informações básicas sobre o veículo do cliente para fornecer uma cotação
# de seguro. Neste momento, o programa deve solicitar ao usuario que insira a marca e o ano
# de fabricação do carro. O programa deve permitir que o usuario insira informações para
# multiplos carros, e ele pode decidir parar de adicionar carros a qualquer momento.

# instruções:

# 1. O programa deve iniciar um loop onde solicitará ao usuario que insira a marca e o ano
# de fabricacao do carro.
# 2. após cada entrada, o programa deve exibir na tela a marca e o ano de fabricação do carro.
# 3. O programa deve continuar a solicitar informações sobre novos carros até que o usuario
# decida parar.
# 4. quando o usuário decidir parar, o programa deve exibir uma mensagem de encerramento,
# e mostrar todos os carros adicionados.

carros = {}

while True:

    marca = input('Insira a marca do carro (sair): ')
    if marca == 'sair':
        break
    ano_fabricacao = int(input('Insira o ano de fabricação (insira 1 para sair): '))
    if ano_fabricacao == 1:
        break

    carros[marca] = ano_fabricacao
    print(carros)

    opcao = input('Deseja continuar? (S/N): ')
    if opcao != 'S':
        break
print(carros)

# código

print('Bem-vindo ao programa de cotação de seguro de automóveis!')
carros = []

while True:
    marca = input('\nDigite a marca do carro (ou digite "parar" para encerrar): ')
    if marca.lower() == 'parar':
        break

    ano_fabricacao = input('Digite o  ano de fabricação do carro: ')

    carro = {'Marca': marca, 'ano-fabricação': ano_fabricacao}
    carros.append(carro)

print('\nObrigado por usar nosso programa de cotação de seguro de automóveis!')
print('Lista de carros adicionados:')
for carro in carros:
    print(f'Marca: {carro['marca']}, Ano de fabricação: {carro['ano-fabricação']}')





