# 8 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin
# a formula de conversao é: K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin

C = float(input('Digite a temperatura em Graus Celsius: '))

K = C + 273.15

print('A temperatura convertida em Kelvin é: {:.2f}'.format(K))
