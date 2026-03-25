# Leia orçamento (float) e gasto (float). Faça orcamento -= gasto.
# Solicite ao usuário que informe o estoque no início do dia (int) e a
# quantidade vendida ao final do dia (int). Atualize a quantidade utilizando 
# atribuição -= para mostrar o estoque final.
estoque = float(input("Digite o valor inicial do seu estoque: "))
qtVendida = float(input("Digite a quantidade vendida: "))

estoque -= qtVendida

print("O estoque restante ao final do dia é:", estoque)
