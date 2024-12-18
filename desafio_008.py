# ============ DESAFIO 008 ============
# Escreva um programa que leia um valor em metros e o exiba convertido em centrimetros e milimetros.

metro = int(input('Digite o numero de metros: '))

centimetros = metro * 100
mili = metro * 1000

print(f'Em {metro} metros tem {centimetros}cm e {mili}mm')

