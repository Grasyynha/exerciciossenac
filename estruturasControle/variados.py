# Peça a idade e mostre: "Maior de idade" ou "Menor de idade"

idade = int(input("Digite a sua idade: "))

if idade > 18:
   print("Você é maior de idade")
else:
  print("Você é menor de idade")

# par ou impar
  
numero = int(input("Digite um numero: "))

if numero % 2 == 0:
    print("O numero é par")
else:
    print("O numero é impar")
    
    
# Peça 2 notas e calcule a média.  Mostre: "Aprovado" (≥ 6) "Reprovado" (< 6) 

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

notas = ( n1, n2)

media = sum(notas) / len(notas)

if media >= 6:
    print("Aprovado")
elif media < 6:
    print("Reprovado")
    
    
# Crie um sistema: Usuário correto: admin  Senha: 1234 Se estiver 
#certo → "Acesso permitido" Se não → "Acesso negado"   