# Desenvolva um programa que permita ao usuario converter uma medida
# de temperatura de uma unidade para outra. O usuario podera escolher entre as
# unidades kelvin e grau celsius para realizar a conversão. Após escolher a unidade
# de origem e inserir a temperatura, o programa exibira o valor convertido para a
# unidade desejada. Utilize as seguintes formulas de conversão.

# de kelvin para celsius:
# celsius = kelvin - 273.15

# de celsius para kelvin:
# kelvin = celsius + 273.15

opcao = int(input('Digite 1 para converter para Kelvin / 2 para converter para Celsius: '))
match (opcao):
    case 1:
        valor = float(input('Insira o valor de graus celsius: '))
        conversao = valor + 273.15
        print(f'O valor de {valor} celsius foi convertido para {conversao:.2f} kelvin.')
    case 2:
        valor = float(input('Insira o valor de kelvin: '))
        conversao = valor - 273.15
        print(f'O valor de {valor} kelvin foi convertido para {conversao:.2f} celsius.')
    case _:
        print('Valor inválido, tente novamente.')