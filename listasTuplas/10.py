# [DICT  - desafio] Agenda (CRUD simples) com ordenação de nomes
# Tarefa: Comece com agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}. 
# Adicionar um novo contato (nome→telefone)
# Atualizar o telefone de um contato informado (se existir)
# Remover um contato pelo nome (se existir)

agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}
print(agenda)

novo_nome = input("Digite o nome do novo contato: ")
novo_telefone = input("Digite o telefone do novo contato: ")
agenda[novo_nome] = novo_telefone

print(agenda)

nome_atualizar = input("Digite o nome do contato que deseja atualizar: ")
telefone_novo = input("Digite o telefone novo: ")

if nome_atualizar in agenda:
    agenda[nome_atualizar] = telefone_novo

nome_remover = input("Digite o nome do contato que deseja remover: ")

if nome_remover in agenda:
    agenda.pop(nome_remover)

print(agenda)

nomes_ordenados = sorted(agenda.keys())
print(nomes_ordenados)