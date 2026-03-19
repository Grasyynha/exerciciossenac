# Leia um número como string e imprima o seu tipo antes e depois de converter para int.
numero = input("Digite um número: ") 
print("Tipo antes da conversão:", type(numero)) 
numero = int(numero) 
print("Tipo depois da conversão:", type(numero))