# Solicite ao usuário que informe os tempos em segundos (int).
#  Converta para minutos inteiros com //= e depois use %= para obter segundos restantes.  
segundos = int(input("Digite o tempo em segundos: "))

minutos = segundos 
minutos //= 60
segundos %= 60

print("Minutos", minutos)
print("Segundos", segundos)