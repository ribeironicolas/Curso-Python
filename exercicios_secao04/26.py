# 26 - Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares.
# A fórmula de conversão é: H = M * 0.0001, sendo M a área em metros quadrados e H
# a área em hectares.

M = float(input('Digite o valor da area em metros quadrados: '))

H = M * 0.0001

print('O valor convertido para hectares é: {:.2f}'.format(H))
