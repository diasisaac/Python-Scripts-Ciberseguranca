import random, string

#tamanho = 16 # boa prática 
tamanho = int(input('Digite o tamanho que voce deseja: ')) 

# recebe a estrutura da senha gerada
# gera na senha letras maiusculas e minusculas
chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+,.;:/?'

# cria outro objeto que pega na bibilitoeca random, chama uma funcao chamada systemrandom que usa a bibiloteca OS que, por sua vez, usa a classe urandom a qual gera numeros aleatorios a partir de fontes fornecidas pelo sistema operacional

# biblioteca os com uso da classe urandom dela
rnd = random.SystemRandom()

# rnd.choice - retorna uma lista com os caracteres randomicos
# cada um caracter gerado pelo chars gere um novo outro 
senha = ''.join(rnd.choice(chars) for i in range(tamanho))

print(f'A senha gerada: {senha}')