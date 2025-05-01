#Desenvolva um programa que leia a largura e a altura de um campo
# de futebol, calcule e exiba a área total do campo e a quantidade
# de grama sintética necessária para cobrir toda a sua superficie.
#Considere que cada rolo de grama sintetica cobre uma área de 5 metros quadrados. m2



def calcular_area(largura,altura):
    area_total = largura * altura
    grama_total = area_total / 5
    return area_total, grama_total

while True:
    try:
        largura_campo = float(input('Insira a largura do campo de futebol: '))
        altura_campo = float(input('Insira a altura do campo de futebol: '))
        break
    except ValueError:
        print('Valores inválidos, use qualquer número inteiro ou real')

resultado = calcular_area(largura_campo,altura_campo)

print(f'A área total do campo de futebol é {resultado[0]} m2.')
print(f'A quantidade necessária de grama sintética para cobrir o campo de futebol são {int(resultado[1])} unidades.')
