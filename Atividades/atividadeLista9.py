# Escreva um programa que solicite ao usuario um numero inteiro positivo
# e calcule o fatorial desse número. Em seguida, exiba o resultado.
# repita o processo até que o usuario decida parar.



repeticao = True
while (repeticao):

    numero_inteiro_positivo = int(input('Insira um número inteiro e maior que 0: '))

    fatorial = 1
    for x in range(1, numero_inteiro_positivo + 1):
        fatorial *= x


    print(f'O fatorial do numero {numero_inteiro_positivo} é {fatorial}')

    repeticao = input('Informe se deseja realizar novamente a operação(S/N): ')

    if repeticao != 'S':
        repeticao = False
