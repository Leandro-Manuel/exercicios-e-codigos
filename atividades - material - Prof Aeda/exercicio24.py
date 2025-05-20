# Um petshop atende 5 cachorros por tarde. Faça um programa que solicite ao usuario
# o codigo do serviço efetuado.

# 1-banho, 2-tosa, 3-banho e tosa, 4-outros

# por fim, exiba a quantidade de solicitacoes para cada um dos serviços.

def menu():
    print('Bem vindo ao Pet Shop!')
    print('Insira 1 - para banho')
    print('Insira 2 - para tosa')
    print('Insira 3 - para banho e tosa')
    print('Insira 4 - outros')
    

menu()
banho = tosa = banho_tosa = outros = 0
for x in range(1,6):
    escolha = int(input(f'[{x}] Escolha uma das opções: '))

    match(escolha):
        case 1:
            banho += 1
        case 2:
            tosa+= 1
        case 3:
            banho_tosa += 1
        case 4:
            outros += 1
        case _:
            print('Opção inválida, tente novamente.')

print('Resumo dos serviços:')
print(f'Tivemos {banho} banho(s) esta tarde!')
print(f'Tivemos {tosa} tosa(s) esta tarde!')
print(f'Tivemos {banho_tosa} banho(s) e tosa(s) esta tarde!')
print(f'Tivemos {outros} outro(s) serviço(s) esta tarde!')

