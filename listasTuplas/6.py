#[DICT] Criar e exibir dicionário de aluno
#  Tarefa: Leia nome e idade. Crie aluno = {"nome": ..., "idade": ...} e exiba o dicionário e 
# seu tipo.  Use: input(), int(), literal {}, acesso por chave dict["chave"], print(), type()


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
aluno = {"nome": nome, "idade": idade}

print(aluno)
print(aluno["nome"])
print("Tipo do dicionário:", type(aluno))
print(aluno["idade"])