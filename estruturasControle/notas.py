
# Crie um programa que receba una nota de 0 a 10
# reprovada
# 5 -6.9  recparecao
# 7 - 8.9 Aprovsfs
# 9 - 10  Aprovada com excelencia

nota = float(input("Digite uma nota: "))

if nota < 5:
    notas = "Recuperação"

elif nota < 7:
    notas = "Aprovada"

else:
    notas = "Aprovada com excelencia"

print(f"Voce está: - {notas}")  
