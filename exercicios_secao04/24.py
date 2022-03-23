# 24 - Leia um valor de área em metros quadrados m² e apresente-o convertido em acres. A
# fórmula de conversão é: A = M * 0,000247, sendo M a área em metros quadrados e A a área em acres.

M = float(input('Digite o valor da area em metros quadrados: '))

A = M * 0.000247

print('O valor da area convertido em acres é: {:.2f} acres'.format(A))
