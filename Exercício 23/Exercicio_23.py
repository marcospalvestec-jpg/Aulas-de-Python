# EXERCÍCIO 23 - CATEGORIA DE VOTAÇÃO

idade = int(input("Idade: "))

if idade < 16:
    categoria = "NÃO PODE VOTAR"
elif idade < 18 or idade >= 70:
    categoria = "VOTO OPCIONAL"
else:
    categoria = "VOTO OBRIGATÓRIO"

print(f"Categoria: {categoria}")
