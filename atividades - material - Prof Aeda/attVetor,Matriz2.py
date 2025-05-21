# Um furto de celular ocorreu na cidade de Recife e Você foi contratado para desenvolver
# um programa que possa ajudar na identificação de uma das pessoas envolvidas.
# Sua tarefa é criar uma solução utilizando vetores que faça cinco perguntas para
# uma pessoa, sendo elas:

# Você conhece a vítima do furto?
# Você esteve no local do furto?
# Você mora perto da vítima?
# A vítima lhe devia?
# Você já trabalhou com a vítima?

# Com base nas respostas, se a pessoa responder positivamente a duas questões,
# ela será classificada como "suspeita". Se responder positivamente a três ou
# quatro questoes, será classificada como "cumplice". Se responder positivamente
# a todas as cinco perguntas, será classificada como "ladrão". Caso contrário,
# será classificada como "inocente".

perguntas = ['Você conhece a vítima do furto?','Você esteve no local do furto?',
             'Você mora perto da vítima?','A vítima lhe devia?','Você já trabalhou'
                                                                ' com a vítima?']
respostas = []
cont = 0
for x in range(5):
    print(perguntas[x])
    resposta = int(input('Insira 1 para sim e 2 para não: '))
    respostas.append(resposta)
    if resposta == 1:
        cont+=1

match(cont):
    case 0:
        print('Inocente')
    case 1:
        print('Inocente')
    case 2:
        print('Suspeita')
    case 3:
        print('Cúmplice')
    case 4:
        print('Cúmplice')
    case _:
        print('Ladrão')

# outro código:
resposta2 = []
contt = 0

print('Responda com sim ou nao para as questões abaixo: ')
resposta2.append(input('Conhece a vitima do furto? '))
resposta2.append(input('esteve no local do furto? '))
resposta2.append(input('Mora perto da vitima? '))
resposta2.append(input('a vitima lhe devia? '))
resposta2.append(input('ja trabalhou com a vitima? '))

for x in resposta2:
    if x == 'sim':
        contt += 1

if contt == 2:
    print('pessoa suspeita')
elif contt == 3 or contt == 4:
    print('pessoa cumplice')
elif contt == 5:
    print('Ladrão')
else:
    print('Inocente')