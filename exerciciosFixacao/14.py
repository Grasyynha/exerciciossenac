# Leia uma quantidade de minutos (int) e converta para horas e minutos (ex.: 130 -> 2h10)
minutos = int(input("Informe os minutos: ")) 
horas = minutos // 60 
resto_minutos = minutos % 60 
print(f"{horas}h{resto_minutos}")