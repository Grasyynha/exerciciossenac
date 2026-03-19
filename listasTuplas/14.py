# [TUPLE] Exibir maior e menor valor
# Tarefa: Leia quatro números inteiros, coloque em uma tupla e exiba o maior e o menor.
# Orientações:  funções: max(), min()  tipos: int, tuple


n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))
n4 = int(input("Digite o quarto numero: "))

numeros = (n1, n2, n3, n4)

print(numeros)

maior = max(numeros)
menor = min(numeros)

print("O maior é: ", maior)
print("O menor é: ", menor)