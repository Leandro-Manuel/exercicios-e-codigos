#Escreva um programa que declare uma variável real para representar uma temperatura em graus celsius.
#atribua um valor a essa variável e converta essa temperatura para fahrenheit usando a formula de conversao

temperatura_graus_celsius = float(input('Informe a temperatura em graus celsius que deseja converter: '))
convertor_fahrenheit = (temperatura_graus_celsius * 9/5) + 32

print(f'{temperatura_graus_celsius}°C equivalem a {convertor_fahrenheit:.1f}°F')