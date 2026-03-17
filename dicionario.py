aluno = {'nome': 'grasiela', 'idade': 46, 'nota': 9.0

}

print(aluno)
print(aluno['nome'])

aluno["turma"] = "93"
print(aluno)
aluno["nota"] = 7.0
print(aluno)

# Criando dicionarios
aluna = {"id": 1, "nome": "Grasiela", "nota": 9.0}
pessoa = {"nome": "Ana", "idade": 46}

# Acessar valores por chave
print("Nome da pessoa:", pessoa["nome"])

# Adicionar e alterar chaves/valores
pessoa["cidade"] = "Palhoça"  # adiciona nova chave
pessoa["idade"] = 26   # altera valor existente
print("Pessoa atualizada:", pessoa)

# Remover chave
removido = pessoa.pop("idade")
print("Valor removido (idade):", removido)
print("Após pop('idade):", pessoa)

# Tamanho
print("Quantidade de chaves em 'aluna':", len(aluna))

# Listar chaves,valores e itens (pares)
print("Chaves de 'aluna':", list(aluna.keys()))
print("Valores de 'aluna':", list(aluna.values()))
print("Itens de 'aluna':", list(aluna.items()))

# Verificar se uma chave existe
print("Chave 'nota' existe?", "nota" in aluna)

# Obter  valor com padrão ( evita erro se  chave não existir)
print("Turma (com default):", aluna.get("turma", "nao cadastrada"))
      
# Atualizar várias chaves de uma vez
aluna.update({"nota": 9.5, "turma": "A" }) 
print("Após update:", aluna)

# Iterar sobre dict
for chave, valor in aluna.items():
    print(f"{chave} -> {valor}")



