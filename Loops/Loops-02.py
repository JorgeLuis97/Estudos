# Exercício 2 - Tabuada:
# Escreva um programa que exiba a tabuada de multiplicação de um número específico fornecido pelo usuário.
n = int(input("Digite um número: "))
for i in range(1, 11):
    resultado = n * i
    print(f"{n} * {i} = {resultado}")
