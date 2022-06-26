#!/usr/bin/env python3

import socket

# bind () associa o socket com seu endereço local [é por isso que o servidor se liga, para que os clientes possam usar esse endereço para se conectar ao servidor.] 
# connect () é usado para se conectar a um endereço [server] remoto, é por isso que o lado do cliente , conectar [ler como: conectar ao servidor] é usado.


# Digo o host e a porta

# O HOST eu posso indicar pelo nome ou endereço ip
HOST = "localhost"
PORT = 5000  # Na porta que o servidor tá escutando pra poder acontecer a comunicação certa.


# IPV4 - AF_INET , SOCK_STREAM - TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Já com o scoket criado, eu crio a conexão

# Um parametro com 2 informações a gente empacota em (())

s.connect((HOST, PORT))

# Vamos fazer o que com essa conexão? Enviar dados

# Codifica a mensagem em string
s.sendall(str.encode("Bom dia Boson"))

# O servidor vai responder pra mim e eu gravo a resposta em uma variável

# Recebe os dados vindo do servidor até um tamanho especificado

data = s.recv(1024)

print(f"Mensagem ecoada: {data.decode()}")
