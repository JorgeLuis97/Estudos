# Exercício 5 - Números primos:
# Escreva um programa que exiba os números primos de 1 a 100.

for i in range(1, 101):
    if (i % i) == 0 and (i % 1) == 0:
        print(f"Número primo: {i}")
