# 18. Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. À
# fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em
# metros cúbicos.

M = float(input('Digite o valor do volume em metros cúbicos: '))

L = 1000 * M

print('O valor convertido para Litros é: {:.2f} m³'.format(L))
