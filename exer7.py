#Escreva um programa que declare duas variaveis reais, uma para representar o peso em quilogrmas
#e outra para representar a altura em metros de uma pessoa. o usuario devera informar os valores.
#calcule o imc da pessao usando a formula: imc = peso / (altura*altura)

peso_pessoa = float(input('Informe o seu peso atual em quilogramas: '))
altura_pessoa = float(input('Informe a sua altura em centimetros: '))

imc_pessoa = peso_pessoa / (altura_pessoa * altura_pessoa)

print(f'O seu IMC atual está em: {imc_pessoa:.1f}')