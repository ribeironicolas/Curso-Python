# 39 - A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
# Sendo que da quantia total:
# O primeiro ganhador receberá 46%;
# O segundo receberá 32%;
# O terceiro receberá o restante;
# Calcule e imprima a quantia ganha por cada um dos ganhadores.

p = 780000 - (780000*0.54)
s = 780000 - (780000*0.68)
t = 780000 - p - s

print(f'O primeiro ganhador irá ganhar {p}, o segundo {s} e o terceiro {t} ')
