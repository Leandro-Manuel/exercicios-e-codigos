# escreva um programa que declare tres variaveis para representar as notas
# de um aluno em uma disciplina. peça ao usuario para informar essas notas e depois
# calcule a media aritmetica. exiba o resultado.

nota1 = float(input('Informe a sua primeira nota: '))
nota2 = float(input('Informe a sua segunda nota: '))
nota3 = float(input('Informe a sua terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print(f'A sua nota média final foi: {media:.1f}')

# Escreva um programa que declare uma variavel inteira para representar a idade
# de uma pessoa. o usuario devera informar a sua idade. verifique se a pessoa é maior
# de idade (idade maior ou igual a 18). exiba uma mensagem indicando o resultado.
# utilizar estrutura boleana v ou f

idadeUser = int(input('Informe a sua idade: '))
print('você é maior de idade.' if idadeUser >= 18 else 'você é menor de idade.')