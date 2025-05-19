# Desenvolva um programa que solicite ao usuario 5 idades dos clientes
# de uma clinica medica e, em seguida, exiba na tela a soma total das
# idades inseridas. Ao finalizar a entrada de dados, o programa deve
# calcular e apresentar a soma das idades dos clientes.

soma_total = 0
for x in range(1,6):
    idade = int(input('Insira sua idade: '))
    soma_total += idade
print(f'A soma total das idades é {soma_total}')