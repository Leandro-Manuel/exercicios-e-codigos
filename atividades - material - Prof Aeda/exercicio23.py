# Voce foi designado a escrever um programa que solicite repetidamente que o
# usuario insira numeros inteiros. O programa deve calcular e exibir a soma
# de todos os numeros inseridos, excluindo qualquer número negativo. O programa
# deve continuar solicitando numeros até que o usuario insira zero para sair.
# Se o usuario inserir um numero negativo, o programa deve exibir uma mensagem
# de erro e solicitar outro numero
somaInteiros = 0


while True:
    numero = int(input('Insira um número (0 - sair): '))
    if numero == 0:
        print(f'A soma dos números é {somaInteiros}')
        break
    elif numero < 0:
        print("Erro, insira um valor positivo!")
        continue
    else:
        somaInteiros += numero

# outro código

total = 0

num = int(input('Insira um numero: '))
while num != 0:
    if num < 0:
        print('numero negativo, insira um valor positivo')
    else:
        total+=num
    num = int(input('Insira um numero: '))

print(f'A soma dos números é {total}')