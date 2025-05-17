# Desenvolva um programa que pergunte a velocidade de um carro.
# Caso a velocidade seja maior que 80km/h, exiba uma mensagem dizendo que o usuario
# foi multado. Nesse caso, exiba o valor da multa, cobrando 5 reais por cada km
# acima da velocidade permitida.

# 2 ações:
# emitir uma mensagem que foi multado e o valor da multa
# emitir uma mensagem que ele estava dentro do limite de velocidade

car_speed = int(input('Informe a velocidade do veículo em km/h: '))
multa = 0
acima = 0

if car_speed > 80:
    acima = car_speed - 80
    multa = acima * 5
    print(f'Veículo acima da via, velocidade: {car_speed} km/h, multa {multa} reais.')
else:
    print('Veículo no limite da via, sem multas')









