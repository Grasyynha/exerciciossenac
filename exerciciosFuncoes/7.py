# Crie uma função que receba uma palavra e verifique
#  se ela é um palíndromo (lê igual de trás para frente).

def palindromo(p):
    return p == p[::-1]

print(palindromo("arara"))