# Solicite ao usuário que informe um número e depois exiba
#  se o número é positivo, negativo ou zero.

numero = int(input("Digite um numero: "))

if numero < 0:
    print("O numero é negativo")
elif numero > 0 :
    print("O numero é positivo")
else:
    print("O numero é zero")        