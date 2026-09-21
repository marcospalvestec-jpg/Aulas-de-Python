'''Exercício 16: Positivo, Negativo ou Zero. Leia um número real e informe se é positivo, negativo ou se o número é igual a zero. 
'''

def traco40():
    print('-'*60,)

traco40()
print(' Vamos descobrir se o número é POSITIVO, NEGATIVO ou ZERO! ')
traco40()



numero = float(input("Digite um número: "))

if numero > 0:
    resultado = "POSITIVO"
elif numero < 0:
    resultado = "NEGATIVO"
else:
    resultado = "ZERO"

print(f"Resultado: {resultado}")
