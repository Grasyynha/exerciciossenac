# Leia o preço de um produto e imprima o preço com 10% de desconto.
produto = float(input("Digite o valor do produto: "))
desconto = produto * 0.10  
valorFinal = produto - desconto 
print("O preço do produto é: " , valorFinal)