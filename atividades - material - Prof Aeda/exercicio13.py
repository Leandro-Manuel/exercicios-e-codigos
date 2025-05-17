# Um sistema de biblioteca precisa calcular a multa para devolucao
# de livros com base na quantidade de dias de atraso. Faça um programa que
# solicite ao usuario o numero de dias de atraso na devolução do livro.
# O programa deve então calcular a multa a ser paga, aplicando as seguintes regras:

# para atrasos de ate 7 dias, a multa é de 0.50 reis por dia
# para atrasos entre 8 e 14 dias, a multa é de 1 real por dia.
# para atrasos acima de 14 dias, a multa é de 2 reais por dia.

def calcular_multa():
    dias_atraso = int(input('Informe a quantidade de dias de atraso: '))

    if dias_atraso > 14:
        valor_multa = dias_atraso * 2
    elif dias_atraso > 8 and dias_atraso <= 14:
        valor_multa = dias_atraso * 1
    else:
        valor_multa = dias_atraso * 0.5

    print(f'Você foi multado em {valor_multa} reais.')

resultado = calcular_multa()