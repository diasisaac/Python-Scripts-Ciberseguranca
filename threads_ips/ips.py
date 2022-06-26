import ipaddress

# importar a biblitoeca ipaddress pra trabalhar
# como manipulacao de ips ( soma, transformar um string pra ip, e etc ) e redes

ip = "192.168.0.1"
endereco = ipaddress.ip_address(ip)
# rede = ipaddress.ip_network(ip)
# print(endereco)
# print(rede) # saber a rede que o ip esta

# Existe o parametro ipaddress.ip_network(ip2, strict=False)

ip2 = "192.168.0.0/24"
rede = ipaddress.ip_network(ip2)
print(rede) # saber a rede que o ip esta

# Saber todos os enderecos de uma rede

for ip2 in rede:
    print(ip2)