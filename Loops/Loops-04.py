# Exercício 4 - Fatorial:
# Escreva um programa que calcule o fatorial de um número fornecido pelo usuário.

n = int(input("Número: "))

for i in range(1, n):
    n *= i

print(f"O Fatorial é {n}")
