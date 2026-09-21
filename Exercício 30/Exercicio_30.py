# EXERCÍCIO 30 - APROVAÇÃO DE EMPRÉSTIMO

valor_imovel = float(input("Valor do imóvel: R$ "))
salario = float(input("Salário mensal: R$ "))
anos = int(input("Prazo em anos: "))

prestacao = valor_imovel / (anos * 12)
limite = salario * 0.30

if prestacao <= limite:
    resultado = "APROVADO"
else:
    resultado = "NEGADO"

print(f"Prestação mensal: R$ {prestacao:.2f}")
print(f"Limite de 30%: R$ {limite:.2f}")
print(f"Resultado: {resultado}")
