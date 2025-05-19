# Desenvolva um programa que possa realizar uma pesquisa para descobrir
# quantas pessoas gostam de futebol. Os usuarios devem responder a pergunta:
# "Voce gosta de futebol?", enquanto os usuarios responderem 'S', o loop continua
# em execução, mas caso respondam 'N', o programa deve encerrar a sua execucao.
# ao final, o programa deve informar quantas pessoas responderam sim.

opcao = True
qtd_gosta = 0
while(opcao):
    pergunta = input('Você gosta de futebol? (S/N): ')
    if pergunta == 'S':
        qtd_gosta += 1
    elif pergunta == 'N':
        opcao = False
    else:
        continue
print(f'A quantidade de pessoas que gostam de futebol são {qtd_gosta} pessoas.')
