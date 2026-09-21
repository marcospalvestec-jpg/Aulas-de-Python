# EXERCÍCIO 28 - É POSSÍVEL FORMAR UM TRIÂNGULO?

lado_1 = float(input("Primeiro lado: "))
lado_2 = float(input("Segundo lado: "))
lado_3 = float(input("Terceiro lado: "))

medidas_positivas = lado_1 > 0 and lado_2 > 0 and lado_3 > 0
regra_triangulo = (
    lado_1 < lado_2 + lado_3
    and lado_2 < lado_1 + lado_3
    and lado_3 < lado_1 + lado_2
)

if medidas_positivas and regra_triangulo:
    resultado = "FORMAM UM TRIÂNGULO"
else:
    resultado = "NÃO FORMAM UM TRIÂNGULO"

print(f"Resultado: {resultado}")
