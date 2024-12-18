# =============== DESAFIO 005 ===============
# Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

soma = n1 + n2
antes = soma - 1
depois = soma + 1

print(f'O sucessor de {soma} é {depois} e o seu antecessor é {antes}!')

