# Simulador de Caixa Eletrônico

conta_usuario = 0
valor_saque = 0
valor_deposito = 0
verificacao = True
confirma_escolha = 'S'



while (verificacao):

    print('---- Bem vindo ao Caixa Eletrônico -----')
    print('Digite 1 para saque / Digite 2 para depósito / Digite 3 para verificar saldo')
    escolha_menu = int(input('Faça sua escolha: '))

    if (escolha_menu == 1):
        confirma_escolha = str(input('1 - Saque, confirma? (S/N): '))
        if (confirma_escolha in 'Ss'):
            valor_saque = float(input('Digite o valor para saque: '))
            if (valor_saque != 0 and valor_saque > 0 and conta_usuario >= valor_saque):
                conta_usuario = conta_usuario - valor_saque
                print(f'Saque realizado no valor de {valor_saque} reais, saldo disponível {conta_usuario} reais.')
            else:
                while (valor_saque > conta_usuario):
                    print(f'Não é possível realizar a operação, seu saldo atual é de {conta_usuario} reais.')
                    valor_saque = float(input('Digite novamente o valor para saque: '))
                if (valor_saque != 0 and valor_saque > 0 and conta_usuario >= valor_saque):
                    conta_usuario = conta_usuario - valor_saque
                    print(f'Saque realizado no valor de {valor_saque} reais, saldo disponível {conta_usuario} reais.')
        else:
            break

    elif (escolha_menu == 2):
        confirma_escolha = str(input('2 - Depósito, confirma? (S/N): '))
        if (confirma_escolha in 'Ss'):
            valor_deposito = float(input('Digite o valor que deseja depositar: '))
            if (valor_deposito != 0 and valor_deposito > 0):
                conta_usuario = conta_usuario + valor_deposito
                print(f'Operação realizada, você depositou {valor_deposito} reais. Seu saldo atual é {conta_usuario} reais.')
            else:
                while(valor_deposito <= 0):
                    print('Valor inválido, insira uma quantidade maior que 0.')
                    valor_deposito = float(input('Informe novamente: '))
                if (valor_deposito != 0 and valor_deposito > 0):
                    conta_usuario = conta_usuario + valor_deposito
                    print(f'Operação realizada, você depositou {valor_deposito} reais. Seu saldo atual é {conta_usuario} reais.')

    elif (escolha_menu == 3):
        confirma_escolha = str(input('3 - mostrar saldo atual, confirma? (S/N): '))
        if (confirma_escolha in 'Ss'):
            print(f'Seu saldo atual é {conta_usuario} reais.')
        else:
            break

    else:
        while(escolha_menu != 1 and escolha_menu != 2):
            escolha_menu = int(input('Valor inválido, insira 1 para saque e 2 para deposito: '))


    confirma_escolha = str(input('Deseja realizar outra operação?(S/N): '))
    if (confirma_escolha in 'Ss'):
        verificacao = True
    else:
        verificacao = False

