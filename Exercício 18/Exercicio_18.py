# EXERCÍCIO 18 - MAIOR DE DOIS NÚMEROS

primeiro = float(input("Primeiro valor: "))
segundo = float(input("Segundo valor: "))

if primeiro > segundo:
    print(f"Maior valor: {primeiro:g}")
elif segundo > primeiro:
    print(f"Maior valor: {segundo:g}")
else:
    print("Resultado: VALORES IGUAIS")
