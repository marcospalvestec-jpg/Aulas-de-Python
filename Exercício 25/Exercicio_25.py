# EXERCÍCIO 25 - PREÇO CONFORME A FORMA DE PAGAMENTO

preco = float(input("Preço: R$ "))
opcao = int(input("Opção de pagamento (1 a 4): "))

if opcao == 1:
    valor_final = preco * 0.90
elif opcao == 2:
    valor_final = preco * 0.95
elif opcao == 3:
    valor_final = preco
elif opcao == 4:
    valor_final = preco * 1.08
else:
    print("OPÇÃO INVÁLIDA")
    raise SystemExit

print(f"Valor final: R$ {valor_final:.2f}")
