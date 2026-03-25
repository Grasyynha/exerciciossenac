# [TUPLE] Contar quantas vezes um número aparece
# Tarefa: Leia quatro números inteiros e crie uma tupla. Depois leia um número e diga quantas 
# vezes ele aparece na tupla.

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))
n4 = int(input("Digite o quarto numero: "))

numeros = (  n1, n2, n3, n4)

procurar = int(input("Digite um numero para procurar: "))

print("O numero escolhido apareceu: ", numeros.count(procurar), "vezes")