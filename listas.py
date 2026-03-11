frutas = ["maça", "banana", "uva"]
numeros = [1,2,3,4]

# Acessando os elementos
print("Primeira fruta:" , frutas[0])
print("Ultima fruta:" , frutas[-1])

# Alterando elementos
frutas[1] = "banana-nanica"
print("Após alteração:" , frutas)

# Adicionando elementos
frutas.append("morango")
frutas.insert(1, "pera")
print("após modificar:", frutas)

# Removendo elementos
frutas.remove("uva")
ultimo = frutas.pop()
print("Após remover  'uva' e pop():", frutas, "| ultima removida:", ultimo)