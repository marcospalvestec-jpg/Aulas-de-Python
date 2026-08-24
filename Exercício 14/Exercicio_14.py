# EXERCÍCIO 14 — TROCA DE VALORES
# Enunciado:
# Leia dois valores inteiros, armazene-os em A e B
# e troque seus conteúdos. Ao final, mostre os
# valores depois da troca
# Requisito:
# Faça a troca utilizando uma variável auxiliar.

a = int(input("A: "))
b = int(input("B: "))
auxiliar = a
a = b
b = auxiliar
print("\nDepois da troca:")
print(f"A: {a}")
print(f"B: {b}")