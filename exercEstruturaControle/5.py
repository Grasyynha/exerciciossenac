# Solicite ao usuário que informe dois números e depois exiba qual número é maior ou se são iguais

n1  =  int(input("Digite o primeiro numero: "))
n2  =  int(input("Digite o segundo numero: "))

if n1 > n2:
    print("O numero maior é: ", n1)
elif n2 > n1:
    print("O numero maior é: ", n2)
else:
    print("Os numeros são iguais")        