# EXERCÍCIO 34 - QUANTIDADE DE DIAS DO MÊS

mes = int(input("Mês (1 a 12): "))
ano = int(input("Ano: "))

if mes < 1 or mes > 12:
    resultado = "MÊS INVÁLIDO"
elif mes == 2:
    bissexto = ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)
    resultado = "29 dias" if bissexto else "28 dias"
elif mes in (4, 6, 9, 11):
    resultado = "30 dias"
else:
    resultado = "31 dias"

print(f"Resultado: {resultado}")
