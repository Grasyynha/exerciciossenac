# Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário.
salario = float(input("Digite o salário: ")) 
percentual = float(input("Digite o percentual de aumento: "))  
aumento = salario * (percentual / 100) 
novo_salario = salario + aumento 
print("O novo salário é: ", novo_salario)