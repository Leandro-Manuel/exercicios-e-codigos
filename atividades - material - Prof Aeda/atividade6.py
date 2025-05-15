# Você foi contratado para desenvolver um sistema simples de calculo
# de notas para uma disciplina. A disciplina possui duas avaliações:

# a primeira avaliação 10 pontos:
# exercicios praticos valem 2 pontos (20% da nota)
# prova pratica valem 8 pontos (80% da nota)

# segunda avaliacao 10 pontos:
# projeto em python vale 10 pontos.

# requisitos:
# implemente um programa que solicite ao usuario a nota dos exercicios praticos de 0 a 2.
# solicite a nota da prova pratica de 0 a 8.
# calcule a nota total da primeira avaliação.
# solicite a nota do projeto da segunda avaliação de 0 a 10.
# calcule a media final da disciplina.

def calcular_nota():
    ex_praticos = float(input('Informe a sua nota dos exercicios praticos (0/2): '))
    prova_pratica = float(input('Informe a sua nota da prova pratica (0/8): '))
    av1 = ex_praticos + prova_pratica
    nota_projeto = float(input('Informe a sua nota no projeto (0/10): '))
    nota_final = (av1 + nota_projeto) / 2

    return nota_final

media_final = calcular_nota()
print(media_final)


