# 32 - Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de
# seu dobro.

num = int(input('Digite um numero inteiro: '))

conta = (num*3+1) + (num*2-1)

print(f'A soma do sucessor de seu triplo com o antecessor de seu dobre é: {conta}')
