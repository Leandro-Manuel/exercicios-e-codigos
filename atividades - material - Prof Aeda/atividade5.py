# O banco central deseja implementar um programa para calcular um bonus
# salarial especial para seus funcionarios. O bonus consiste em um acrescimo de
# 10% sobre o salario mensal de cada funcionario.

# escreva um programa que solicite ao usuario que insira o valor do salario mensal
# de um funcionario. Em seguida, o programa deve calcular o bonus de 10% com base
# no salario informado e imprimir na tela o salario inicial, o salario final(incluindo o bonus)
# e o valor do acrescimo recebido pelo funcionario.


salario_mensal = float(input('Informe o salário do funcionário: '))

def calcular_valor(salario_mensal):
    bonus = salario_mensal * 0.1
    salario_final = salario_mensal + bonus
    return salario_final, bonus

salario_final = calcular_valor(salario_mensal)[0]
bonus = calcular_valor(salario_mensal)[1]

print(f'O salário inicial foi de {salario_mensal}, com bonus o salario final foi {salario_final}, o valor do bonus {bonus}')



