# 10 - Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s
# (metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em
# km/h e M em m/s.

K = float(input('Digite a velocidade em Km/h (quilometros por hora): '))

M = K/3.6

print('A velocidade convertida em metro por segundo é: {:.2f} m/s'.format(M))
