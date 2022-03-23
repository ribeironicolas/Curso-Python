# 48 - Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.

seg = int(input('Digite um valor em segundos: '))

h = seg / 3600
rest = seg % 3600
m = rest / 60

print('Horas: {:.2f} \nMinutos: {:.2f} \nSegundos: {:.2f}'.format(h, m, seg))
