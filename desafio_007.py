# ============ DESAFIO 07 ============
# Desenvolva um programa que leia as duas notas de um aluno, calcule mostre a sua média.

print('==== Informações do Aluno ====')
nome = input('Digite o nome: ')

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'A média do Aluno {nome} é: {media}')

