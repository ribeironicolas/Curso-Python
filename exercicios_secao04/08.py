# 8 - Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius
# a formula de conversao é: C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin

K = float(input('Digite a temperatura em Graus Kelvin: '))

C = K - 273.15

print('A temperatura convertida em Celsius é: {:.2f}'.format(C))

