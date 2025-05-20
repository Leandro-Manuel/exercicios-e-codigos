# Bruna é uma cientista dedicada que está conduzindo uma pesquisa sobre o pH de varias
# substancias. Para facilitar sua analise, ela precisa de um programa que receba como
# entrada uma serie de valores representando o pH de cada substancia. O programa continuara
# solicitando valores até que -1 seja inserido, indicando o fim da entrada. Para
# cada valor inserido, o programa determinara se a substancia é acida
# (pH maior igual a 0 e pH menor que 7), basica(pH maior que 7), neutra(pH igual a 7).

while True:
    valor_pH = int(input('Insira o pH da substância: '))
    if valor_pH >= 0 and valor_pH < 7:
        print('Substância ácida')
    elif valor_pH > 7:
        print('Substância de acidez básica')
    elif valor_pH == 7:
        print('Substância neutra')
    else:
        print('Não classificado')

    if valor_pH == -1:
        break
