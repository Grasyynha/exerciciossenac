
temp  = int(input("Digite a  temperatura atual: "))


if temp < 10:
    temperatura = "Muito frio"

elif temp <= 10:
    temperatura = "Agradável"

elif temp < 25:
    temperatura = "Quente"
    
else:
    temperatura = "Muito quente"            


print(f"A temperatura está: - {temperatura}")            
