# Desenvolva um programa que pergunte a velocidade de um carro.
# caso a velocidade ultrapasse 80km/h, exiba uma mensagem dizendo
# que o usuario foi multado. Nesse caso, exiba o valor da multa, cobrando
# 5 reais por cada km acima da velocidade permitida.

# Emitir uma mensagem que foi multado e o valor da multa.
# Encerrar o programa

acima = 0
valor = 0
velocidade = int(input('informe a velocidade do veiculo: '))
if velocidade > 80:
    acima = velocidade - 80
    valor = acima * 5
    print(f'Você está acima da via, velocidade {velocidade} km/h, multado em {valor} reais.')
else:
    print('Velocidade está dentro do limite da via, não foi multado')


