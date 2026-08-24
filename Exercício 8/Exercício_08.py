# EXERCÍCIO 08 — DESCONTO NO PRODUTO
#
# Enunciado:
# Leia o preço de um produto. Calcule um desconto
# de 10% e mostre o valor do desconto e o preço final.
#
# Regras:
# Desconto = preço * 0.10
# Preço final = preço - desconto

preco = float(input("Preço: R$ "))

desconto = preco * 0.10
preco_final = preco - desconto

print(f"Desconto: R$ {desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")