def cadastrar_paciente():
    nome = input('Informe o seu nome: ')
    idade = int(input('Informe a sua idade: '))
    especialidade = int(input('Especialidade: 1.Cardiologia, 2.pediatria, 3.clinica geral: '))
    convenio = input('Você tem convênio? (sim/nao): ')

    return nome,idade,especialidade,convenio

def calcular_valor(idade,especialidade,convenio):

    if especialidade == 1:
        valor = 200
        if convenio == 'sim':
            valor_desconto = valor * 0.5
            if idade <12 or idade > 65:
                valor_desconto = valor * 0.6
            valor_final = valor - valor_desconto
    elif especialidade == 2:
        valor = 150
        if convenio == 'sim':
            valor_desconto = valor * 0.5
            if idade <12 or idade > 65:
                valor_desconto = valor * 0.6
            valor_final = valor - valor_desconto
    else:
        valor = 100
        if convenio == 'sim':
            valor_desconto = valor * 0.5
            if idade <12 or idade > 65:
                valor_desconto = valor * 0.6
            valor_final = valor - valor_desconto

    return valor_final



