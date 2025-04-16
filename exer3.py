#Escreva um programa que declare uma variável do tipo real para representar uma quantia em dolares.
#solicite ao usuario que insira essa quantia e, em seguida, converta-a para reais, utilizando um fator
#de conversão fixo. exiba o resultado.

valor_dolar = float(input('informe a quantidade de dolares que deseja converter para real: '))

cotacao_real = 6

resultado = valor_dolar * cotacao_real
print('O valor em reais para receber é: ',resultado)


