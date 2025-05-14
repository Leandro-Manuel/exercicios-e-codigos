# Escreva um programa que declare uma variavel real para representar uma
# temperatura em graus celius. Atribua um valor a essa variavel e converta essa
# temperatura para fahrenheit usando a formula de conversão. exiba o resultado

g_celsius = 25
fahrenheit = (g_celsius * 9 / 5) + 32
print(f'{g_celsius}C equivalem a {fahrenheit}F')


# Escreva um programa que declare duas variaveis reais, uma para representar o peso
# em quilogramas e outra para representar a altura em metros de uma pessoa.
# o usuario devera informar os valores. calcule o imc da pessoa usando a formula
# imc = peso / (altura * altura). exiba o resultado

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))

imc = peso / (altura * altura)
print(f'O seu imc está em {imc:.2f}')