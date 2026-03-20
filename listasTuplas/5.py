# [LIST - desafio] Fila: chegadas, prioridade e atendimento
# Tarefa: Inicie fila = ["Ana", "Bruno"]. Leia dois nomes e adicione (use extend). 
# Leia um cliente prioritário e insira na posição 1. Atenda (remova e capture) 
# o primeiro com pop(0). Exiba a fila a cada etapa.
# Use: input(), extend(), insert(), pop(), print()
# Tipos: str, list.
# Conceitos: estrutura de fila, operações de inserção/remoção, ordem.

fila = ["Ana", "Bruno"]

# Ler dois nomes e adicionar
nome1 = input("Digite um nome: ")
nome2 = input("Digite outro nome: ")

fila.extend([nome1, nome2])
print("Fila após adicionar:", fila)

# Cliente prioritário
prioritario = input("Digite o nome do cliente prioritário: ")
fila.insert(1, prioritario)
print("Fila com prioritário:", fila)

# Atender primeiro da fila
atendido = fila.pop(0)
print("Atendido:", atendido)
print("Fila final:", fila)
