#[DICT - desafio] Atualizar preço e quantidade; calcular o total 
# Tarefa: Leia produto = {"nome": str, "preco": float, "quantidade": int}. 
# Aplique aumento percentual ao preço e some 2 unidades na quantidade. Calcule total =
#  preco * quantidade e exiba.  Use: float(), int(), input(), acesso/atribuição por chave, print()

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade: "))

produto = {"nome": nome, "preco": preco, "quantidade": quantidade}

# Aumento percentual (exemplo: 10%)
aumento = float(input("Digite o percentual de aumento (%): "))
produto["preco"] = produto["preco"] * (1 + aumento / 100)

# Somar 2 unidades
produto["quantidade"] = produto["quantidade"] + 2

# Calcular total
total = produto["preco"] * produto["quantidade"]

print("Produto atualizado:", produto)
print("Total:", total)