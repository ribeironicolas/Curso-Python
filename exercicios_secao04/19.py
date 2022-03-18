# 19 - Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³. A
# fórmula de conversão é: M = L/1000, Sendo L o volume em litros e M o volume em metros
# cúbicos.

L = float(input('Digite o valor do volume em litros: '))

M = L/1000

print('O valor convertido para metros cúbicos é: {:.2f} m³'.format(M))