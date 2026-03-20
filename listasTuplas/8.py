# Tarefa: Leia produto = {"nome": str, "preco": float}. Tente remover a chave "desconto" 
# se existir, sem gerar erro. Mostre antes e depois.


nome = input("Digite o nome do produto: ")
preco = float(input("Digite o valor do produto: "))

produto = {"nome": nome, "preco": preco}

print("Anterior:", produto)

produto.pop("desconto", None)

print("Posterior:", produto)