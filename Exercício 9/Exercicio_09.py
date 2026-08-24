# EXERCÍCIO 09 — REAJUSTE SALARIAL
#
# Enunciado:
# Leia o salário atual de um funcionário.
# Calcule um aumento de 15% e mostre o valor
# do aumento e o novo salário.
#
# Regras:
# Aumento = salário atual * 0.15
# Novo salário = salário atual + aumento

salario_atual = float(input("Salário atual: R$ "))

aumento = salario_atual * 0.15
novo_salario = salario_atual + aumento

print(f"Aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")