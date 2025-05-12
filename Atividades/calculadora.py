#Faça uma calculadora, que faça as 4 operações aritméticas e exponenciação

escolha_numeros = 0.0
numeros = []

print('----- Calculadora -----')
print('Digite 1 para somar / Digite 2 para Subtrair / Digite 3 para Dividir / Digite 4 para Multiplicar / Digite 5 para Exponenciação ')

escolha_menu = int(input('Escolha uma das opções: '))

def switch_case(escolha_menu):
    match escolha_menu:
        case 1:
            escolha_numeros = float(input('Informe a quantidade de números que deseja somar: '))
            for i in range(1,escolha_numeros):
                numeros[escolha_numeros] = float(input('Digite o número: '))





            return escolha_numeros
        case 2:
            escolha_numeros = float(input('Informe a quantidade de números que deseja somar: '))
            return escolha_numeros
        case _:
            print('Opção inválida')




