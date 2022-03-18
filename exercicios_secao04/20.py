# 20 - Leia um valor de massa em quilogramas e apresente-o convertido em libras. À fórmula
# de conversão é: L = K/0.45, sendo K a massa em quilogramas e L a massa em libras.

K = float(input('Digite o valor da massa em quilogramas: '))

L = K/0.45

print('O valor convertido para Libras é: {:.2f}'.format(L))