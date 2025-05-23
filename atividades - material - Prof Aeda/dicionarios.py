# O que é dicionario?
# Uma estrutura de dados que permite armazenar pares de chave-valor.
# semelhante a uma lista, mas os indices são substituidos por chaves unicas.

# sintaxe:
# nome_do_dicionario = {chave1: valor1, chave2: valor2 ... chaveN: valorN}

agenda = {'Leandro': 24, 'Manuel': 32, 'Francisco': 30}
print(agenda)
agenda = {'Athena': 19, 'Manuel': 20, 'Leandro': 23, 'Lu': 20}
print(agenda)
print(agenda['Lu'])

# e se o contato não existir?
# print(agenda['José']) - error, não existe chave josé
# os dicionarios possuem um método especifico para busca de valores,
# o get(), no qual podemos passar como parametros a chave que queremos e um valor
# padrão para retornar caso essa chave não seja encontrada
print(agenda.get('José','Não encontrado'))
# usando a chave para atribuir um novo valor
agenda['José'] = 42
print(agenda)

# removendo um valor do dicionario - utilizando pop()
agenda.pop('Leandro')
print(agenda)

# Você foi designado para criar um programa simples para armazenar contatos em uma agenda.
# O programa deve solicitar ao usuario que insira o nome e o número de telefone de um
# contato e, em seguida, armazená-los em um dicionario. O usuario pode continuar
# adicionando contatos a agenda até decidir sair do programa.

agenda_contatos = {}
while True:
    try:
        nome = input('Insira o seu nome: ')
        telefone = int(input('Insira o seu número de telefone: '))
        agenda_contatos[nome] = telefone
    except ValueError:
        print('Valores inválidos, tente novamente')
        continue

    opcao = input('Deseja continuar? (S/N): ')
    if opcao != 'S':
        print('Encerrando o programa...')
        break
print(agenda_contatos)

alunos = {
    'Alice': [8, 7, 9],
    'Bob': [6, 8, 7],
    'João': [9, 8, 10]
}

for nome in alunos:
    media = sum(alunos[nome]) / len(alunos[nome])
    print(f'A média de {nome} é {media:.2f}')



