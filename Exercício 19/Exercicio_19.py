# EXERCÍCIO 19 - MAIOR E MENOR DE TRÊS NÚMEROS

numero_1 = float(input("Primeiro valor: "))
numero_2 = float(input("Segundo valor: "))
numero_3 = float(input("Terceiro valor: "))

maior = numero_1
menor = numero_1

if numero_2 > maior:
    maior = numero_2
if numero_3 > maior:
    maior = numero_3

if numero_2 < menor:
    menor = numero_2
if numero_3 < menor:
    menor = numero_3

print(f"Maior: {maior:g}")
print(f"Menor: {menor:g}")
