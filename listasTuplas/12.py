#[TUPLE] Acessar elementos da tupla
#  Tarefa: Leia três frutas e coloque em uma tupla. Depois leia uma fruta e diga se ela 
# está ou não na tupla. Orientações:  usar in usar input()
 

f1 = input("Digite a primeira fruta: ")
f2 = input("Digite a segunda fruta: ")
f3 = input("Digite a terceira fruta: ")

frutas = (f1, f2, f3)

print(frutas)

procurar = input("Digite uma fruta para procurar: ")

print("Está na tupla?", procurar in frutas)