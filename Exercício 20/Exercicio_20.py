# EXERCÍCIO 20 - TRÊS VALORES EM ORDEM CRESCENTE

numero_1 = int(input("Primeiro valor: "))
numero_2 = int(input("Segundo valor: "))
numero_3 = int(input("Terceiro valor: "))

if numero_1 > numero_2:
    numero_1, numero_2 = numero_2, numero_1
if numero_1 > numero_3:
    numero_1, numero_3 = numero_3, numero_1
if numero_2 > numero_3:
    numero_2, numero_3 = numero_3, numero_2

print(f"Ordem crescente: {numero_1}, {numero_2}, {numero_3}")
