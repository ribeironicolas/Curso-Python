# 14 - Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
# é: R= G* π/180, sendo G o ângulo em graus e R em radianos e π = 3.14.

G = float(input('Digite o angulo em graus: '))

R = G * 3.14/180

print('O valor convertido para radianos é: {:.2f}'.format(R))
