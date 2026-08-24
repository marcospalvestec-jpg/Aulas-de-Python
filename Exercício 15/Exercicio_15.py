# EXERCÍCIO 15 — CUSTO FINAL DA COMPRA
#
# Enunciado:
# Leia o preço unitário de um produto, a quantidade
# comprada e o valor do frete. Mostre o subtotal
# dos produtos e o valor total da compra.
#
# Regras:
# Subtotal = preço unitário * quantidade
# Total = subtotal + frete

preco_unitario = float(input("Preço unitário: R$ "))
quantidade = int(input("Quantidade: "))
frete = float(input("Frete: R$ "))

subtotal = preco_unitario * quantidade
total = subtotal + frete

print(f"\nSubtotal: R$ {subtotal:.2f}")
print(f"Total: R$ {total:.2f}")