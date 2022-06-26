#!/usr/bin/env python3

# bind () associa o socket com seu endereço local [é por isso que o servidor se liga, para que os clientes possam usar esse endereço para se conectar ao servidor.] 
# connect () é usado para se conectar a um endereço [server] remoto, é por isso que o lado do cliente , conectar [ler como: conectar ao servidor] é usado.

import socket

# O HOST eu posso indicar pelo nome ou endereço ip
HOST = "localhost"
PORT = 5000

# Vou criar uma variavel s de socket e invocar o metodo socket do objeto socket importado lá em cima

# Passa os parametros -> (familia de protocolo, tipo de protocolo)

# IPV4 - AF_INET , SOCK_STREAM - TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# O objeto ainda não tem os valores vinculados. Não sabe qual é o endereço do server e a porta que ele vai escutar. Daí a gente vai colocar

s.bind((HOST, PORT))

# O metodo bind recebe 1 parametro, daí a gente divide ele em 2 partes com o (()) pra ser um parametro só.

# Até agora vinculamos o host e o port como nosso socket. Próximo, vamos colocar no modo de escuta

# Agora, o servidor está no modo de escuta
s.listen()

print("Aguardando conexão de um cliente")

# O servidor precisa aceitar a conexão quando ela chegar. Daí vamos criar 2 elementos: conexao e endereco

# Esses 2 elementos serão o retorno de s.accept que é o método pra aceitar a conexão

# Esses retornos é o padrão do método accept

# O padrão do método accept é retornar primeiro a conexão e depois o endereço
conexao, endereco = s.accept()

# Vai mostrar a porta que está conectada com o nossso cliente
print(f"Conectado em {endereco}")

# Agora que está conectado queremos trocar mensagens. As msgs podem ter vários tamanhos, maior, menor, fragmentada...

# Vamos usar o while

while True:

    # Crio uma variável data pra passar o tamanho que eu espero receber em bytes.
    data = conexao.recv(1024)

    # Vou usar um if pra verificar se os dados terminaram

    # Se não tiver nada em data
    if not data:

        print("Fechando a conexão")
        conexao.close()
        break

    # Se tiver dados

    # O cliente vai mandar uma msg pro servidor e eu vou ecoar ela de volta pro cliente
    conexao.sendall(data)  # com isso eu posso saber se foi enviado a resposta
