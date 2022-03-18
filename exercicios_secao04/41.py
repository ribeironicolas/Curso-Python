# 41 - Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
# trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre
# o valor calculado.

valor = float(input('Digite o valor da hora de trabalho em reais: '))
hora = float(input('Digite o total de horas trabalhadas no mes: '))

total = valor*hora*1.10

print('O valor total a ser pago ao funcinario é: R${:.2f}'.format(total))

