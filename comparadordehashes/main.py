import hashlib

# Crie 2 arquivos a serem comparados

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

# recebe da haslib um construtor new o qual passamos pra ele o algoritmo de hash que será usado
hash1 = hashlib.new('sha256')

# Agora, diremos para o programa qual arquivo abrir pra comparar o hash

# o update() faz a comparacao do hash e dentro dele eu passo a informacao a ser comparada

hash1.update(open(arquivo1, 'rb').read()) # hash do primerio arquivo

# hash do arquivo 2
hash2 = hashlib.new('sha256')

hash2.update(open(arquivo2, 'rb').read())

# Agora, vamos fazer a comparacao entre os hashes

# hexdigest() resume o hash em hexadecimal
print(f'O hash do arquivo 1: {hash1.hexdigest()}')
print(f'O hash do arquivo 2: {hash2.hexdigest()}')

# a funcao digest resume os dados  passados pelo metodo update. 
if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')

else:
    print(f'O arquivo: {arquivo1} é igual ao arquivo: {arquivo2}')