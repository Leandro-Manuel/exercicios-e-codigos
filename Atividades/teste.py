#receba o valor de um produto e a porcentagem de desconto e retorne o valor do produto com desconto

valor_original_produto = int(input('Informe o valor do produto: '))
valor_porcentagem = int(input('Informe a quantidade de desconto: '))

valor_desconto = (valor_porcentagem / 100) * valor_original_produto

valor_final_produto = valor_original_produto - valor_desconto

print(valor_final_produto)

