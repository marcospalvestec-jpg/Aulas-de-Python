# EXERCÍCIO 35 - VALOR DO INGRESSO

PRECO_INTEIRO = 30.00

idade = int(input("Idade: "))
estudante = input("Estudante (SIM/NÃO): ").strip().upper()

tem_meia_entrada = idade < 12 or estudante == "SIM" or idade >= 60
valor_ingresso = PRECO_INTEIRO * 0.50 if tem_meia_entrada else PRECO_INTEIRO

print(f"Valor do ingresso: R$ {valor_ingresso:.2f}")
