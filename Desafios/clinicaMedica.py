import os
valor = 0
maiorValor = 0
valorTotal = 0
nomeMaior = None
idade = 0
convenio = None
qtdCardiologia = qtdPediatria = qtdClinicaGeral = 0
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

                if convenio == 'sim':
                    convenio = True
                    break
                elif convenio == 'não':
                    convenio = False
                    break
                else:
                    continue
            return nome_paciente, idade_paciente, especialidadeMed, convenio
        except ValueError:
            print('Valores inválidos, tente novamente...')
        break

def valor_consulta():
    global valor, especialidadeMed, convenio, idade
    match (especialidadeMed):
        case 1:
            valor = 100
        case 2:
            valor = 150
        case 3:
            valor = 200

    if convenio == True:
        valor = valor - (valor * 0.5)

    if idade < 12 or idade > 65:
        valor = valor - (valor * 0.1)

    return valor

def relatorio(a,b,c,d,e,f):
    print('---- RELATÓRIO FINAL -----')
    print('Total de atendimentos:')
    print(f'Clínica Geral: {a}')
    print(f'Pediatria: {b}')
    print(f'Cardiologia: {c}')
    print(f'O valor total arrecadado foi {d} reais.')
    print(f'Paciente com o maior pagamento: {e} ({f} reais).')

def boas_vindas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('--------- Bem vindo ao sistema de gestão de pacientes --------')
    input('Pressione Enter para continuar')

def menu():
    while True:
        try:
            boas_vindas()
            global valor, maiorValor, valorTotal, nomeMaior, qtdCardiologia, qtdPediatria, qtdClinicaGeral, idade, convenio

            dados = cadastrar_paciente()
            nome = dados[0]
            idade = dados[1]
            especialidadeMed = dados[2]
            convenio = dados[3]

            match (especialidadeMed):
                case 1:
                    qtdCardiologia += 1
                case 2:
                    qtdPediatria += 1
                case 3:
                    qtdClinicaGeral += 1

            valor = valor_consulta()
            if valor > maiorValor:
                maiorValor = valor
                nomeMaior = nome

            valorTotal += valor
            print(f'{nome}, o valor da sua consulta são {valor} reais.')

            continuar = input('Deseja realizar a operação novamente? (sim / não): ')
            if continuar != 'sim':
                relatorio(qtdClinicaGeral, qtdPediatria, qtdCardiologia, valorTotal, nomeMaior, maiorValor)
                break

        except ValueError:
            print('Valores incorretos, tente novamente...')
            continue





