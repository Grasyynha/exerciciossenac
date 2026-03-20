# [DICT - CONTINUIDADE DO EXERCÍCIO ANTERIOR] 
# Adicionar uma nova chave nota
# Tarefa: Partindo de um aluno com nome e idade, leia uma nota (float) e adicione a 
# chave "nota". Exiba o dicionário.  Use: float(), input(), atribuição dict["nota"] = valor, 
# print()


aluno = {'nome': 'grasiela', 'idade': 46}

nota = float(input("Digite a sua nota: "))
aluno["nota"] = nota
print(aluno)

