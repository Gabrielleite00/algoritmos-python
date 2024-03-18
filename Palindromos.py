# Recebe a palavra do usuário
palavra = input("Digite uma palavra: ")

# Inverte a palavra
palavra_invertida = palavra[::-1]

# Verifica se a palavra é um palíndromo
if palavra == palavra_invertida:
    print("A palavra", palavra, "é um palíndromo.")
else:
    print("A palavra", palavra, "não é um palíndromo.")
