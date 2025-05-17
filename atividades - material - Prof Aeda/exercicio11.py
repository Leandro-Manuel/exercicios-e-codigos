# Uma empresa de entrega deseja calcular o custo do frete com base na distancia
# da entrega e no peso da encomenda. crie um programa que solicite ao usuario a distancia
# da entrega em km e o peso da encomenda em kg. o programa deve entao calcular o custo
# do frete, aplicando as seguintes regras:

# para distancias acima de 100km, o custo do frete é de 2 reais por km.
# para distancias menores ou iguais a 100km, o custo do frete é de 1,50 reais por km.
# alem disso, para encomendas com peso superior a 10 kg, há uma taxa de 5 reais.

def calcular_frete():
    distancia = float(input('Insira a distância da entrega(km): '))
    peso = float(input('Insira o peso do produto(kg): '))

    if distancia <= 100:
        frete = distancia * 1.5
    else:
        frete = distancia * 2

    if peso > 10:
        frete += 5

    print(f'Total a ser pago: {frete} reais.')

resultado = calcular_frete()