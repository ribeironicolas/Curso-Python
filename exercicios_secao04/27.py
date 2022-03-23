# 27 - Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
# A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H
# a área em hectares.

H = float(input('Digite o valor da area em hectares: '))

M = H * 1000

print('O valor convertido em metros quadrados é: {:.2f} m²'.format(M))

