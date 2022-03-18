# 13. Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de
# conversão é: M = K/1,61 sendo K a distância em quilômetros e M em milhas.

K = float(input('Digite a distancia em quilometros: '))

M = K/1.61

print('A distancia convertida em milhas é: {:.2f} milhas'.format(M))
