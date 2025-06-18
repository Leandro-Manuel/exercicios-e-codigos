import os
def cadastrar_paciente():
    while True:
        try:
            nome_paciente = input('Insira o seu nome: ')
            idade_paciente = int(input('Insira a sua idade: '))
            while True:
                especialidadeMed = int(input('Qual é a sua especialidade? (1 - cardiologia, 2 - pediatria, 3 - clinica geral): '))
                if (especialidadeMed != 1) and (especialidadeMed != 2) and (especialidadeMed != 3):
                    continue
                else:
                    break
            while True:
                convenio = input('Você tem convênio médico? (sim / não): ')
                if convenio != 'sim' and convenio != 'não':
                    continue
                else:
                    break
            return nome_paciente, idade_paciente, especialidadeMed, convenio
        except ValueError:
            print('Valores inválidos, tente novamente...')
        break

def valor_consulta():
    global valor
    match (especialidadeMed):
        case 1:
            valor = 100
        case 2:
            valor = 150
        case 3:
            valor = 200

    if convenio == 'sim':
        valor = valor - (valor * 0.5)

    if idade < 12 or idade > 65:
        valor = valor - (valor * 0.1)

    return valor

def boas_vindas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('--------- Bem vindo ao sistema de gestão de pacientes --------')
    input('Pressione Enter para continuar...')
while True:
    boas_vindas()
    valor = 0

    dados = cadastrar_paciente()
    idade = dados[1]
    especialidadeMed = dados[2]
    convenio = dados[3]

    valor = valor_consulta()

    print(f'O valor total da sua consulta é {valor} reais.')

    continuar = input('Deseja realizar a operação novamente? (sim / não): ')
    if continuar != 'sim':
        break



