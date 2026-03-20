#[LIST - desafio] Notas: subtituir a menor nota, ordenar e recalcular a média
# Tarefa: Leia três notas (float) em uma lista. Calcule a média. Substitua a menor nota por 
# uma nova informada. Ordene a lista e mostre a nova média.
# Use: float(), input(), min(), list.index(), atribuição por índice, sort(), sum(), len(),
#  print()
# Tipos: float, list.
# Conceitos: mutabilidade, ordenação in-place, média aritmética.

notas = []

for i in range(3):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

print("Antes:", notas)

menor = min(notas)
posicao = notas.index(menor)

nova_nota = float(input("Nova nota: "))
notas[posicao] = nova_nota

notas.sort()
print("Depois:", notas)

#n1 float(input("Digite a primeira nota"))
#n2 float(input("Digite a primeira nota"))
#n3 float(input("Digite a primeira nota"))

# notas = [n1,n2,n3]
# print(notas)
# mediaInicial = sum(notas)/len(notas)
# menorNota  = min(notas)
# indiceMenor = lista.index(menorNota)
# novaNota = float(input("Digite a nova nota")
# notas[indiceMenor] = novaNota
# print(notas)
# notas.sort


