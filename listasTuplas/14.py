lista = []
for i in range(4):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista.append(numero)

# Mostrar o tamanho da lista antes da remoção
print("Tamanho antes:", len(lista))

# Passo 2: Ler o valor alvo
alvo = int(input("Digite o valor a remover, se existir: "))

# Passo 3: Remover o valor se estiver na lista
if alvo in lista:
    lista.remove(alvo)

# Mostrar o tamanho da lista depois da remoção
print("Tamanho depois:", len(lista))
