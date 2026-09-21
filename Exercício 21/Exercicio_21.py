# EXERCÍCIO 21 - APROVADO OU REPROVADO

nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
media = (nota_1 + nota_2) / 2

if media >= 7:
    situacao = "APROVADO"
else:
    situacao = "REPROVADO"

print(f"Média: {media:.1f}")
print(f"Situação: {situacao}")
