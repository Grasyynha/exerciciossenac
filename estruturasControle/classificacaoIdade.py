# Classificação de idade  peça a idade e classifique:  0–12 → Criança  13–17 → Adolescente
# 18+ → Adulto

idade  = int(input("Digite a sua idade: "))

if idade < 12:
    categoria = "Criança"

elif idade < 17:
    categoria = "Adolescente"
    
else:
    categoria = "Adulto"

print(f"Vocè é: - {categoria}")   


  