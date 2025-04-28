# Simulador de Caixa Eletrônico

import sys

conta_usuario = 0
verificacao = True

historico_saque = []
historico_deposito = []
contagem_historico = 0

while (verificacao):

    print('---- Bem vindo ao Caixa Eletrônico -----')
    print('Digite 1 para saque / Digite 2 para depósito / Digite 3 para verificar saldo / 4 - consultar histórico')
    escolha_menu = int(input('Faça sua escolha: '))

    if (escolha_menu == 1):
        confirma_escolha = str(input('1 - Saque, confirma? (S/N): '))
        if (confirma_escolha in 'Ss'):
            valor_saque = float(input('Digite o valor para saque: '))
            if (valor_saque > 0 and conta_usuario >= valor_saque):
                conta_usuario -= valor_saque
                contagem_historico += 1
                print(f'Saque realizado no valor de {valor_saque} reais, saldo disponível R$ {conta_usuario}')
                historico_saque += [contagem_historico,'saque',valor_saque,'reais']
            else:
                while (valor_saque > conta_usuario):
                    print(f'Não é possível realizar a operação, seu saldo atual é de R$ {conta_usuario}')
                    valor_saque = float(input('Digite novamente o valor para saque: '))
                if (valor_saque > 0 and conta_usuario >= valor_saque):
                    conta_usuario -= valor_saque
                    contagem_historico += 1
                    print(f'Saque realizado no valor de {valor_saque} reais, saldo disponível R$ {conta_usuario} .')
                    historico_saque += [contagem_historico,'saque', valor_saque, 'reais']
        else:
            print('Encerrando o programa...')
            sys.exit()

    elif (escolha_menu == 2):
        confirma_escolha = str(input('2 - Depósito, confirma? (S/N): '))
        if (confirma_escolha in 'Ss'):
            valor_deposito = float(input('Digite o valor que deseja depositar: '))
            if (valor_deposito > 0):
                conta_usuario += valor_deposito
                contagem_historico += 1
                print(f'Operação realizada, você depositou R$ {valor_deposito}. Seu saldo atual é R$ {conta_usuario}')
                historico_deposito += [contagem_historico,'deposito',valor_deposito, 'reais']
            else:
                while(valor_deposito <= 0):
                    print('Valor inválido, insira uma quantidade maior que 0.')
                    valor_deposito = float(input('Informe novamente: '))
                if (valor_deposito > 0):
                    conta_usuario += valor_deposito
                    contagem_historico += 1
                    print(f'Operação realizada, você depositou {valor_deposito} reais. Seu saldo atual é R$ {conta_usuario}')
                    historico_deposito += [contagem_historico,'deposito', valor_deposito, 'reais']

    elif (escolha_menu == 3):
        confirma_escolha = str(input('3 - mostrar saldo atual, confirma? (S/N): '))
        if (confirma_escolha in 'Ss'):
            print(f'Seu saldo atual é {conta_usuario} reais.')
        else:
            print('Encerrando o programa...')
            sys.exit()

    elif (escolha_menu == 4):
        confirma_escolha_quatro = str(input('4 - Consultar histórico, confirma? (S/N): '))
        if (confirma_escolha_quatro in 'Ss'):
            if historico_deposito:
                print(historico_deposito)
            else:
                print('Não há registro de saque')

            if historico_saque:
                print(historico_saque)
            else:
                print('Não há registro de deposito')
        else:
            print('Encerrando o programa...')
            sys.exit()
    else:
        print('Opção inválida')
        sys.exit()

    confirma_escolha = str(input('Deseja realizar outra operação?(S/N): '))
    if (confirma_escolha in 'Ss'):
        verificacao = True
    else:
        verificacao = False

