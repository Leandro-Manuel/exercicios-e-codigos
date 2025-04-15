# receba dois numeros e faça as quatro operações aritméticas de acordo com a preferencia do usuario

print('Escolha uma das opções: ')
print('1 - Somar dois números')
print('2 - Subtrair dois números')
print('3 - multiplicar dois números')
print('4 - dividir dois números')

escolha = int(input('Faça a sua escolha: '))

if escolha>=1 and escolha<=4:
    nmr1 = int(input('Escreva um número maior que 0: '))
    nmr2 = int(input('Escreva outro número maior que 0: '))
    if nmr1 > 0 and nmr2 > 0:
        if escolha == 1:
            resultado = nmr1 + nmr2
            print('A soma dos dois números é:',resultado)
        elif escolha == 2:
            resultado = nmr1 - nmr2
            print('A soma dos dois números é:', resultado)
        elif escolha == 3:
            resultado = nmr1 * nmr2
            print('A soma dos dois números é:', resultado)
        else:
            resultado = nmr1 / nmr2
            print('A soma dos dois números é:', resultado)
    else:
        print('O número deve ser maior que 0')
else: print('Escolha entre 1 e 4')
