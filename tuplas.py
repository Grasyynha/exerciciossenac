dias = ("segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo")
print(dias)
print(dias[0])
print(dias[-1])

# Tamanho
print(len(dias))

# Fatiamento em tuplas
print("Primeiros 3 dias", dias[:3])

# Verificar se um elemento em tuplas
print("Tem 'segunda'?", "segunda" in dias)

# Contagem e indice em tuplas
print("Contagem de 'terça':", dias.count("terça"))
print("Contagem de indice de 'quarta':", dias.index("quarta"))

