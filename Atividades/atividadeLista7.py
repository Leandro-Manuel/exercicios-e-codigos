# Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final
# quantos homens foram cadastrados
#a idade da mulher mais velha
# a média da idade do grupo(ambos os sexo)
# quantas mulheres tem mais de 20 anos

qtd_homens = 0
qtd_mulheres = 0
soma_idade_homens = 0
soma_idade_mulheres = 0
mulheres_mais_20 = 0
mulher_mais_velha = 0

for x in range(5):
    sexo_pessoa = input('Qual é o seu sexo? (M - masculino / F - feminino): ')
    idade_pessoa = int(input('Informe a sua idade: '))

    if sexo_pessoa == 'M':
        qtd_homens += 1
        soma_idade_homens += idade_pessoa
    else:
        if idade_pessoa > 20:
            mulheres_mais_20 += 1

        soma_idade_mulheres += idade_pessoa
        qtd_mulheres += 1
        if idade_pessoa > mulher_mais_velha:
            mulher_mais_velha = idade_pessoa

media_idade_homens = soma_idade_homens / qtd_homens
media_idade_mulheres = soma_idade_mulheres / qtd_mulheres

print(f'A quantidade de homens cadastrados foram {qtd_homens}')
print(f'A idade da mulher mais velha foi {mulher_mais_velha}')
print(f'A idade média do grupo dos homens foi {media_idade_homens:.2f} anos, e das mulheres {media_idade_mulheres:.2f} anos.')
print(f'A quantidade de mulheres que tem mais de 20 anos foi {mulheres_mais_20}.')
