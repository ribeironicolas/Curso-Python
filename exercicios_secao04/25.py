# 25 - Leia um valor de área em acres e apresente-o convertido em metros quadrados m².
# A fórmula de conversão é: M = A * 4048,58, sendo M a área em metros quadrados e A a área em acres.

A = float(input('Digite o valor da area em acres: '))

M = A * 4048.58

print('O valor convertido para metros quadrados é: {:.2f} m²'.format(M))
