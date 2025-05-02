# Desenvolva um programa que seja capaz de calcular a média ponderada
# de um aluno. Inicialmente solicite o nome e as três notas do aluno,
# logo após, calcule e exiba na tela a média. Na média ponderada, considere
# os seguintes pesos nas notas: 2, 3 e 5.

# Logo após verifique e informe o status do aluno na disciplina baseado
# nas seguintes informações:

# media até 4.9 - reprovado / media até 5.0 e 6.9 - recuperação
# media 7.0 ou superior - aprovado

nome_aluno = input('Escreva o seu nome: ')

nota1_aluno = float(input('Insira a sua primeira nota: '))
nota2_aluno = float(input('Insira a sua segunda nota: '))
nota3_aluno = float(input('Insira a sua terceira nota: '))

media_notas = (nota1_aluno + nota2_aluno + nota3_aluno) / 3
media_ponderada_notas = (nota1_aluno * 2) + (nota2_aluno * 3) + (nota3_aluno * 5) / 10

print(f'Sua nota média foi {media_notas}.')

if (media_notas <= 4.9):
    print(f'A sua média final foi {media_notas}, você foi reprovado.')
elif (media_notas >= 5 and media_notas <= 6.9):
    print(f'A sua média final foi {media_notas}, você está em recuperação.')
else:
    print(f'A sua média final foi {media_notas}, você está aprovado.')
