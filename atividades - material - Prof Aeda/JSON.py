# O que é um arquivo Json
# JSON (JavaScript Object Notation) é um formato leve de troca de dados
# facil de ler e escrever para humanos
# facil de interpretar e gerar maquinas

# Python oferece suporte nativo para leitura, manipulação e escrita de arquivos JSON,
# uma estrutura de dados popular para armazenamento e transmissão de informações.

# criar um arquivo Json, importar a biblioteca e criar o arquivo.

import json
import os

arquivo_nome = "C:\\Users\\niifh\\Códigos-em-Python\\atividades - material - Prof Aeda\\dados.json"

# verifica se o arquivo existe

if not os.path.exists(arquivo_nome):
    # cria um arquivo JSON vazio
    with open(arquivo_nome, 'w') as arquivo:
        json.dump({},arquivo) # dados iniciais com um dicionario vazio

# escrevendo em arquivos Json
# Criar dicionario
# escrever o dicionario no json
dados = {
    '123': {
        'nome': 'Joao',
        'idade': 12
    },
    '345': {
        'nome':'Renan',
        'idade': 34
    }
}

# criar dicionario, escrever o dicionario no json
with open(arquivo_nome, 'w') as arquivo:
  json.dump(dados,arquivo,indent=4)

# Adicionar novo item
dados['456'] = {'nome': 'Maria', 'idade': 25}
# Atualizar item existente
dados['345']['idade'] = 35
with open(arquivo_nome, 'w') as arquivo:
  json.dump(dados,arquivo,indent=4)

# lendo arquivos Json, importar biblioteca, ler o arquivo
with open(arquivo_nome, 'r') as arquivo:
    dados = json.load(arquivo)
print(dados)

#manipulação de dados Json
# excluindo um valor, pode utilizar os comandos del, pop e remove

if '123' in dados:
    del dados['123']

print(dados)
