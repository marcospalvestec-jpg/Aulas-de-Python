# EXERCÍCIO 07 — CELSIUS PARA FAHRENHEIT
#
# Enunciado:
# Leia uma temperatura em graus Celsius e mostre
# o valor equivalente em Fahrenheit.
#
# Regra:
# Fahrenheit = Celsius * 9 / 5 + 32

celsius = float(input("Temperatura em °C: "))

fahrenheit = celsius * 9 / 5 + 32

print(f"Temperatura em °F: {fahrenheit:g}")