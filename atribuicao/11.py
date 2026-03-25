# Solicite ao usuário uma distância em metros e depois converta para km inteiros com //= 1000, 
# guarde os metros restantes utilizando %= (utilize outra variável).
metros = int(input("Digite a distancia em metros: "))  
distancia = metros
distancia //= 1000

metros_restantes = metros
metros_restantes %= 1000

print("Quilmetros", metros)
print("Metros restantes", metros_restantes)