# 6 - Leia uma temperatura em graus Celsius e apresenta-a convertida em graus Fahrenheit
# a formula da conversao é: F = C * (9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit
# e C a temperatura em Celcius

C = float(input('Digite a temperatura em Graus Celsius: '))

F = C * (9/5) + 32

print(f'A temperatura convertida em Fahrenheit é: {F}')
