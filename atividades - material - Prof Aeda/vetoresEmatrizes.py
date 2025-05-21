# vetor (lista ou array) é uma estrutura de dados composta por uma quantidade
# determinada de elementos de qualquer tipo primitivo.

vetor = [1,4,'abc',18.15,True,False]
vetor[0] = 10
vetor.insert(2,'abcdef')
vetor.pop()
vetor.append(500)
vetor.remove(True)
vetor.pop(0)
print(vetor)

numbers = [0,6,4,2,60,22,19,13]

numbers.sort()
print(numbers)
print(len(vetor))

# comandos básicos:

# Substituindo um valor existente: nome_do_vetor[indice] = novo_valor
# Adicionar um novo valor: nome_do_vetor.append(novo_valor)
# Ordenar em ordem crescente: nome_do_vetor.sort()
# Ordenar em ordem decrescente: nome_do_vetor.sort(reverse=True)
# Contar quantidade de valores: len(nome_do_vetor)
# Adicionar um valor em um índice específico: nome_do_vetor.insert(indice,valor)
# Remover o último valor: nome_do_vetor.pop(), remover valor pelo índice .pop(indice)
# Remover um valor pelo conteúdo: nome_do_vetor.remove(valor)

# Desenvolva um programa que receba do usuario cinco valores inteiros e guarde
# em um vetor(lista). ao final, mostre os valores na tela.

lista = []
for x in range(5):
    lista.append(int(input('Digite um valor: ')))
print(lista)

# Desenvolva um programa que receba valores inteiros e guarde em um vetor(lista).
# O programa deve continuar solicitando valores até que o usuário insira o valor 0
# para indicar o fim da entrada. Ao final, mostre os valores na tela.

list2 = []
while True:
    numero = int(input('Digite um número inteiro (0 - sair): '))
    if numero != 0:
        list2.append(numero)
    else:
        print('Encerrando o programa...')
        break
print(list2)

# as funções min(), max() e sum(), encontram o menor valor da lista, maior valor da
# lista e realiza a soma de todos os elementos da lista, respectivamente.

notas = [6.0,4.0,3.5,9.0]

print(min(notas))
print(max(notas))
print(sum(notas))
print(f'A média da nota foi {sum(notas) / len(notas)}')

# Matrizes são estruturas de dados que possuem linhas e colunas
# nome_matriz = [[tamanhoX], [tamanhoY]]
# referenciacao = nome_matriz = [posiçãoX][posiçãoY]

matriz = [[0, 0], [0, 0]]

matriz2 = [
    [0, 0],
    [0, 0]
]

matriz[0][0] = 1
matriz[0][1] = 2
matriz[1][0] = 3
matriz[1][1] = 4

for linha in matriz:
    print(linha)
print(matriz)

# adicionar valores em uma matriz 2x4, exibir a matriz na tela

matriz2x4 = [[], []]

for linha in range(2):
    for coluna in range(4):
        matriz2x4[linha].append(int(input(f"Digite o valor para posição [{linha}] [{coluna}]: ")))

for linha in matriz2x4:
    print(linha)