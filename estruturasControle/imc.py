
peso = float(input("Digite o seu peso em (kg): "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura ** 2)

if imc  < 18.5:
    categoria = "Magreza"
elif imc < 25:
    categoria = "Normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidade"

print(f"Imc = {imc:.2f}  - {categoria}")            
