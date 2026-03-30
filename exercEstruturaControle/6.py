# Faça uma calculadora simples contendo as operações: soma, subtração, divisão e multiplicação. 
# Solicite ao usuário que informe dois número e que informe também a operação que deseja 
# realizar 
# (+, -, /, *) e depois exiba o resultado.

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

operacao = input("Digite a operação (+, -, /, *): ")

if  operacao == "+":
    resultado = n1 + n2

elif operacao == "-":
    resultado = n1 - n2
    
elif operacao  == "/":
    resultado = n1 / n2
elif operacao == "*":
    resultado = n1 * n2  
else:
    print("Operação inválida")
    resultado = None

if resultado is not None:
    print(f"O resultado da operação é: {resultado}")    

