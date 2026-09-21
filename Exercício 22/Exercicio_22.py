# EXERCÍCIO 22 - SITUAÇÃO DO ALUNO POR FAIXA

nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
media = (nota_1 + nota_2) / 2

if media < 5:
    situacao = "REPROVADO"
elif media < 7:
    situacao = "RECUPERAÇÃO"
else:
    situacao = "APROVADO"

print(f"Média: {media:.1f}")
print(f"Situação: {situacao}")
