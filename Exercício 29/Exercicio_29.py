# EXERCÍCIO 29 - TIPO DE TRIÂNGULO

lado_1 = float(input("Primeiro lado: "))
lado_2 = float(input("Segundo lado: "))
lado_3 = float(input("Terceiro lado: "))

forma_triangulo = (
    lado_1 > 0
    and lado_2 > 0
    and lado_3 > 0
    and lado_1 < lado_2 + lado_3
    and lado_2 < lado_1 + lado_3
    and lado_3 < lado_1 + lado_2
)

if not forma_triangulo:
    resultado = "NÃO FORMA TRIÂNGULO"
elif lado_1 == lado_2 == lado_3:
    resultado = "EQUILÁTERO"
elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
    resultado = "ISÓSCELES"
else:
    resultado = "ESCALENO"

print(f"Resultado: {resultado}")
