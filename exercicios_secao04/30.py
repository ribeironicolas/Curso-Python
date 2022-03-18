# 30 - Leia um valor em real e a cotacao do dólar. Em seguida, imprima
# o valor correspondente em dólares.

real = float(input('Digite a quantia em real: '))
dolar = float(input('Digite a cotacao do dolar atual: '))

cambio = real * dolar

print(f'{real} reais em dólares é: {cambio}')
