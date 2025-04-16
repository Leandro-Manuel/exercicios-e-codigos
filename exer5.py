#escreva um programa que delcare uma variavel inteira para representar a idade de uma pessoa.
#o usuario devera informar a sua idade. verifique se a pessoa é maior de idade (idade maior ou igual a 18.

idade_pessoa = int(input('Informe a sua idade: '))

if idade_pessoa >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')