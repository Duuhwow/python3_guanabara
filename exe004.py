# =============== Exercicio 004 ===============
# Fça um programa que leia  algo pelo teclado e mostre na tela o seu tipo primitivo,
# e todas as informações possiveis sobre ele.

entrada = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(entrada))
print('Só tem espaços?', entrada.isspace())
print('É um número?', entrada.isnumeric())
print('É alfabético?', entrada.isalpha())
print('É alfanumérico?', entrada.isalnum())
print('Está em maiúsculas?', entrada.isupper())
print('Está em minúsculas?', entrada.islower())
print('Está capitalizada?', entrada.istitle())


