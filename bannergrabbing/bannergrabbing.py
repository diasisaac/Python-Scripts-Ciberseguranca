import socket
import os
import sys


# Função Banner Grabbing com socket
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        banner = s.recv(1024)

        return banner.decode()

    except TimeoutError:
        return 'Error Timed out'


# Checa vulnerabilidade -
def checkVulns(banner, filename):
    with open(filename, 'r') as f:
        # Coleta cada serviço vulnerável que temos conhecimento
        for line in f.readlines():
      
            # Procura na String banner se se o serviço listado na variavel line está nela
            if line in banner:
                print(f'[+] Server is vulnerable: {line}')
                break


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]

        if not os.path.isfile(filename):
            print(f'[-] {filename} does not exists')
            exit(0)

        if not os.access(filename, os.R_OK):
            print(f'[-] {filename} access denied')
            exit(0)

        else:
            print(f'[-] Usage: {str(sys.argv[0])} <vuln filename>')

            portlist = [21, 22]
            
            # you put an ip here
            ip = "x.x.x.x"

            for port in portlist:

                banner = retBanner(ip, port)

                checkVulns(banner, filename)

    else:
        print("Complete it")

if __name__ == "__main__":
    main()

#print(retBanner("10.0.0.121", 21))


