# Leia um contador (int) e um passo (int). Faça contador += passo duas vezes. Mostre o resultado.
#Solicite ao usuário que informe um orçamento (float) e um gasto (float).
#  Utilize atribuição -= para descontar o gasto do orçamento.
orcamento = float(input("Informe o seu orçamento: "))
gasto = float(input("Informe o seu gasto: "))

orcamento -= gasto
print("Você ainda tem:", orcamento)
