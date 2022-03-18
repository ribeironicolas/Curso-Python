# 40 - Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite
# o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
# paga, sabendo-se que são descontados 8% para imposto de renda.

dias = int(input('Digite o numero de dias trabalhados: '))

print(f'Devera ser pago pelo servico um total de: R${(dias*30)*0.92}')
