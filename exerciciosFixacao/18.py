# Leia um nome e uma nota (float), com uma casa decimal, e imprima:
# Aluno <nome> ficou com nota <nota> 
nome = input("Digite seu nome: ") 
nota = float(input("Digite a sua nota: ")) 
print(f"Aluno(a) {nome} ficou com nota: {nota:.1f}")