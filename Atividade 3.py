'''
Docstring para equacao03
Três amigos somaram suas idades. 
João tem o dobro da idade de Pedro. 
Carlos tem a mesma idade de Pedro. 
A soma das idades é 60 anos. Qual é a idade de cada um?
'''
# Definição do problema:
# Idade de Pedro = P
# Idade de João = 2 * P
# Idade de Carlos = P
# A soma das idades é 60: P + 2P + P = 60

# Resolvendo a equação:
# 4P = 60
# P = 60 / 4
# P = 15

# atribuindo as idades para resolução da equação

idade_pedro = 15
idade_joao = 2*idade_pedro
idade_carlos = idade_pedro

#Confirmar a conta

soma_idades = idade_pedro + idade_joao + idade_carlos

#Resultados

print(f"A Idade de Pedro {idade_pedro} anos")
print(f"A Idade de João {idade_joao} anos")
print(f"A Idade de Carlos {idade_carlos} anos")
print(f"A soma das idades é de {soma_idades} anos")
