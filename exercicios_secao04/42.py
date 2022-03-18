# 42 - Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-
# se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso,
# ele paga 7% de imposto sobre o salário-base.

sal = float(input('Digite o salario-base: '))
grat = sal*5/100
imp = sal*7/100

total = sal + grat - imp

print('O valor a ser recebido sera de: R${:.2f}'.format(total))
