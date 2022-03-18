# 43 - Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
# o total a pagar com desconto de 10%;
# o valor de cada parcela, no parcelamento de 3x sem juros;
# a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
# e a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

valor = float(input('Digite o valor total do pedido: '))
desc = valor*0.90
par = valor/3

print(f'O valor com 10% de desconto é: R${desc}')
print('O valor de cada parcela em 3x sem juros é: {:.2f} cada'.format(par))
print(f'Comissao do vendedor (venda a vista): {desc*1.05 - desc}')
print(f'Comissao do vendedor (venda parcelada): {valor*1.05 - valor}')
