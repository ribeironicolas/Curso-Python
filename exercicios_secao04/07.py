# 7 - Leia uma temperatura em graus Fahrenheit e apresenta-a convertida em graus Celsius
# a formula da conversao é: C = 5.0 * (F - 32.0)/9.0, sendo F a temperatura em Fahrenheit
# e C a temperatura em Celcius

F = float(input('Digite a temperatura em Graus Fahrenheit: '))

C = 5 * (F - 32) / 9

print('A temperatura convertida em Celsius é: {:.2f}'.format(C))
