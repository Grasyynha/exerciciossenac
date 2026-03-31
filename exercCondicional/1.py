# Enunciado: Peça para o aluno digitar a idade de uma pessoa e o
#  programa deve classificar:
#  0–12 → Criança
# 13–17 → Adolescente
# 18–59 → Adulto
# 60+ → Idoso

idade = int(input("Digite a sua idade: "))

if idade  <= 12:
    print("Você é Criança")
elif idade <= 17:
    print("Você é Adolescente")    
elif idade <= 59:
    print("Você é adulto")
else:
    print("Você é idoso")        