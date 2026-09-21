# EXERCÍCIO 24 - ANO BISSEXTO

ano = int(input("Ano: "))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    resultado = "BISSEXTO"
else:
    resultado = "NÃO BISSEXTO"

print(f"Resultado: {resultado}")
