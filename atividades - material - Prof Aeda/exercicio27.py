# Você foi contratado por um banco para desenvolver um programa que automatize
# a análise de solicitações de empréstimo para a compra de uma casa. O programa
# solicitará ao usuário o valor da casa desejada, o salário do comprador e o prazo de
# pagamento em anos. Com base nessas informações, o programa calculará o valor da
# prestação mensal e verificará se ela não excede 30% do salário do comprador.
# Se a prestação mensal estiver dentro desse limite, o emprestimo será aprovado.
# caso contrário, será negado.

# especificações:

# O programa deve solicitar ao usuario o seguinte:
# o valor da casa desejada
# o salario do comprador
# o prazo de pagamento em anos
# o programa calculara o valor da prestação mensal
# o programa continuara a solicitar os dados do usuario e realizar a analise de
# emprestimo até que o usuário decida encerrar o programa.

opcao = 'S'
while opcao.upper() == 'S':
    try:
        valor_casa = float(input('Insira o valor total da casa: '))
        salario = float(input('Insira o seu salário: '))
        prazo_ano = int(input('Insira o prazo de pagamento em anos: '))

        if valor_casa <= 0 or salario <= 0 or prazo_ano <= 0:
            print("Erro: Valores devem ser positivos. Tente novamente.\n")
            continue

        qtd_mes = prazo_ano * 12
        prestacao_mensal = valor_casa / qtd_mes
        limite_aprovacao = salario * 0.30

        if prestacao_mensal > limite_aprovacao:
            print(
                f'Crédito negado. A prestação (R${prestacao_mensal:.2f}) excede 30% do seu salário (R${limite_aprovacao:.2f}).\n')
        else:
            print('Empréstimo aprovado!')
            print(f'Valor da prestação mensal: R${prestacao_mensal:.2f}\n')

    except ValueError:
        print("Erro: Insira apenas números válidos.\n")
        continue

    opcao = input('Deseja realizar uma nova análise? (S/N): ')

print("Programa encerrado. Obrigado!")
