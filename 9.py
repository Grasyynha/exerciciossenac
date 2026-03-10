# Solicite um valor de estoque (int), subtraia as vendas utilizando -= e 
# depois a reposição do estoque utilizando +=, por fim, aplique %= 6. 
estoque = int(input("Digite o valor do estoque: "))
vendas = int(input("Digite o valor de vendas: "))
reposicao = int(input("Digite o valor da reposição: "))
estoque -= vendas
estoque += reposicao
estoque %= 6

print("Estoque final", estoque)