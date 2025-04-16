#Escreva um programa que declare tres variaveis reais para representar as notas de um aluno
# em uma disciplina. Peça ao usuario para informar essas notas e depois calcule a media aritmetica.

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))

media_notas = (nota1 + nota2 + nota3) / 3

print(f'Sua nota final foi: {media_notas:.1f}')