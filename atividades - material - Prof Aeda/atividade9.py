# Desenvolva um programa que pergunte a velocidade de um carro.
# Caso a velocidade seja maior que 80km/h e menor que 100km/h, exiba uma
# mensagem dizendo que o usuario foi multado. Nesse caso, exiba o valor da multa,
# cobrando 5 reais por cada km acima da velocidade permitida.
# Caso a velocidade seja maior ou igual a 100km/h, exiba uma mensagem
# dizendo que o usuario foi multado. Nesse caso, exiba o valor da multa,
# cobrando 10 reais por cada km acima da velocidade permitida.

# emitir uma mensagem que foi multado e o valor da multa.
# emitir uma mensagem que ele estava dentro do limite da velocidade

speed_car = int(input('Informe a velocidade do veículo em km/h: '))
acima = multa = None

if speed_car >= 100:
    acima = speed_car - 80
    multa = acima * 10
    print(f'Excesso de velocidade, multado em {multa}')
elif (speed_car > 80 and speed_car < 100):
    acima = speed_car - 80
    multa = acima * 5
    print(f'Excesso de velocidade, multado em {multa}')
else:
    print('No limite da via, sem multa')