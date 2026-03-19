#[TUPLE - desafio] Organizar valores sem mexer na tupla original
# Tarefa: Leia quatro números em uma tupla e exiba: a tupla original
# uma lista ordenada apenas para visualização o tipo da variável ordenada
#Objetivo: mostrar diferença entre tupla e lista sem precisar modificar nada.
# Use: sorted(), print(), type()

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))
n4 = int(input("Digite o quarto numero: "))

numeros = (n1, n2, n3, n4)

print(numeros)
lista_ordenada = sorted(numeros)
print(lista_ordenada)