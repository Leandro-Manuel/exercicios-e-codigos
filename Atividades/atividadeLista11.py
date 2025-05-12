# Controle de presença em curso gratuito de tecnologia

# Um centro comunitario está oferecendo um curso gratuito de introducao a tecnologia
# com duração total de 10 encontros presenciais. Para receber o certificado de conclusão,
# cada aluno precisa ter participado de pelo menos 6 encontros.

# voce foi convidado a desenvolver um programa que ajude os organizadores a
# controlar a presença dos alunos e verificar quem tem direito ao certificado.

# o programa deve: receber o nome de varios alunos (o numero total de alunos será
# informado no inicio)
# para cada aluno, solicitar a quantidade de encontros frequentados (um numero
# de 0 a 10.

# ao final, exibir:
# A lista dos alunos que tem direito ao certificado.
# a porcentagem de alunos aprovados (ou seja, que compareceram a 4 encontros ou mais)

qtdAlunos = int(input('Insira a quantidade total de alunos cadastrados: '))
lista = []
qtd_aprovados = 0

for _ in range(qtdAlunos):
    nomeAluno = input('Informe o nome do aluno: ')
    frequencia = int(input('Informe a presença total do aluno: '))

    if frequencia >= 6:
        lista.append(nomeAluno)
    elif frequencia >= 4 and frequencia <= 5:
        qtd_aprovados += 1

porcentagem_alunos_aprovados = (qtd_aprovados * 100) / qtdAlunos

print('Alunos com direito ao certificado:')
for aluno in lista:
    print(aluno)
print(f'A porcentagem de alunos certificados: {porcentagem_alunos_aprovados} %')

