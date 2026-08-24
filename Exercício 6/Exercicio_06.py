# EXERCÍCIO 06 — ÁREA E PERÍMETRO DO RETÂNGULO
#
# Enunciado:
# Leia a largura e a altura de um retângulo.
# Mostre a área e o perímetro.
#
# Regras:
# Área = largura * altura
# Perímetro = 2 * (largura + altura)

largura = float(input("Largura: "))
altura = float(input("Altura: "))

area = largura * altura
perimetro = 2 * (largura + altura)

print(f"Área: {area:g}")
print(f"Perímetro: {perimetro:g}")