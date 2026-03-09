# Leia saldo (float) e depósito (float). Use saldo += deposito e mostre o novo saldo.
# Solicite ao usuário que informe o saldo da sua conta e o valor que será depositado;
#  ambos os valores devem ser do tipo FLOAT. Utilize atribuição += para adicionar o deposito 
# ao saldo  da conta e exiba o novo saldo na tela.
saldo = float(input("Informe o saldo de sua conta: "))
deposito = float(input("Digite o valor a ser depositado: "))

saldo += deposito
print("Novo saldo em conta é: ", saldo)