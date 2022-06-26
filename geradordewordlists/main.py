import itertools

# boa fonte teorica - https://www.geeksforgeeks.org/python-itertools-permutations/

texto = input("Palavra a ser permutada/combinada: ")
tamanho = int(input("Digite o tamanho da palavra resultada: "))

# o permutations é quem faz a permutação dos caracteres no wordlist
# o primeiro parametro é o texto e o segundo é o número de permutações
lista_resultado = itertools.permutations(texto, tamanho)

for i in lista_resultado:
    #  eu junto cada caracter com o proximo
    #  Pega um caracter da string, roda, gera outro e junta.
    # Isso é realmente aleatorio?
    print(f'Cada linha da lista - i: {i}')
    print('Caracteres da linha i juntado pela funcao join: ')
    print(''.join(i))
