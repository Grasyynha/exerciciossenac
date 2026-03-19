#[LIST] Atualizar elemento com uma operação
# Tarefa: Crie uma lista com três inteiros. Atualize o último elemento para a soma dos dois primeiros. Exiba a lista.
# Use: int(), input(), indexação lista[i], print()
# Tipos: int, list.
# Conceitos: operadores aritméticos (+), acesso/atribuição por índice.

numeros = [int(input("Digite o 1º número: ")),
           int(input("Digite o 2º número: ")),
           int(input("Digite o 3º número: "))]

numeros[2] = numeros[0] + numeros[1]

# Mostrar a lista final
print(numeros)
