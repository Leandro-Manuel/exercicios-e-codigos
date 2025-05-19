# Desenvolva um programa que solicite ao usuario as idades dos clientes de uma clinica medica, e em seguida,
# exiba na tela a soma total das idades inseridas. O programa deve continuar solicitando as idades até que o
# usuario decida parar de inserir dados. Ao finalizar a entrada de dados. o programa deve calcular e
# apresentar a soma das idades dos clientes.

opcao = 'S'
user_age = soma_ages = 0
while(opcao != 'N'):
    user_age = int(input('Insira sua idade: '))
    soma_ages += user_age
    opcao = input('Continuar?(S/N): ')
print(f'A soma das idades foi {soma_ages}')