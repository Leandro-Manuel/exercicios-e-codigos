# Um determinado sistema solicita que o usuario insira dois valores inteiros.
# Logo apos, o sistema apresenta tres opcoes de operacoes que poderao ser executadas,
# o usuario precisa escolher uma delas 1 - soma, 2 - multiplicacao, 3 - subtracao.
# Caso contrário, se for uma opcao invalida, o sistema precisa notificar.

# mostrar a soma dos valores
# mostrar a multiplicacao dos valores
# mostrar a subtracao dos valores
# opcao invalida

def calcular_valores():
    valor1 = int(input('Digite um valor inteiro: '))
    valor2 = int(input('Digite outro valor inteiro: '))
    opcao = int(input('[1]Somar, [2] Multiplicar, [3]subtrair, [4]dividir:  '))

    match (opcao):
        case 1:
            resultado = valor1 + valor2
            print(f'A soma dos dois números é {resultado}')
        case 2:
            resultado = valor1 * valor2
            print(f'A multiplicação dos dois números é {resultado}')
        case 3:
            resultado = valor1 - valor2
            print(f'A subtração dos dois números é {resultado}')
        case 4:
            resultado = valor1 / valor2
            print(f'A divisão dos dois números é {resultado}')
        case _:
            print('Opção inválida, tente novamente.')

resultado = calcular_valores()

