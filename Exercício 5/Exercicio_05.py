# EXERCÍCIO 05 — CONVERSÃO DE MEDIDAS
#
# Enunciado:
# Leia uma medida em metros e mostre o valor
# equivalente em centímetros e milímetros.
#
# Regra:
# 1 metro = 100 centímetros = 1.000 milímetros.

metros = float(input("Metros: "))

centimetros = metros * 100
milimetros = metros * 1000

print(f"Centímetros: {centimetros:g}")
print(f"Milímetros: {milimetros:g}")