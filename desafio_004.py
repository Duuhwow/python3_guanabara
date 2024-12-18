# ============ DESAFIO 04 ============

#DESCRIÇÃO:
#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

n1 = input('Escreva algo: ')

print('Este é o tipo do que você escreveu', type(n1))
print('Ele é um numero decimal?', n1.isdecimal())
print('Ele está em maiusculo?', n1.isupper())
print('Ele é um espaço vazio?', n1.isspace())
print('Ele é Alpha numerico?', n1.isalnum())
print('Ele é um numero?', n1.isnumeric())
print('Ele em minusculo?', n1.islower())




