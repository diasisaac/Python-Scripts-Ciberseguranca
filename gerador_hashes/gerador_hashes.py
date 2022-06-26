import hashlib

def main():

    print('''### MENU - ESCOLHA O TIPO DE HASH ### 
            1 -  MD5
            2 -  SHA1
            3 -  SHA256
            4 -  SHA512 
            5 -  Sair do Programa
            Digite o numero de hash a ser gerado ou 5 para sair do programa: ''')

    escolha = int(input('Escolha: '))

    return escolha

def opcao_escolhida(escolha):
    texto = input('Digite o texto para ser gerada a hash: ')

    if escolha == 1:
        # passa uma string pra trasnformar em hash
        # passa um b'' pra converter pra bytes
        resultado = hashlib.md5(texto.encode('utf-8'))
        print(f'Hash da string: {resultado.hexdigest()}')

    elif escolha == 2: # SHA1
        resultado = hashlib.sha1(texto.encode('utf-8'))
        print(f'Hash da string: {resultado.hexdigest()}')
  
    elif escolha == 3: # SHA256
        resultado = hashlib.sha256(texto.encode('utf-8'))
        print(f'Hash da string: {resultado.hexdigest()}')

    elif escolha == 4: # SHA512
        resultado = hashlib.sha512(texto.encode('utf-8'))
        print(f'Hash da string: {resultado.hexdigest()}')





if __name__ == "__main__":
    

    while True:
    
        escolha = main()

        if escolha == 5:
            print("Saindo do programa... ")
            break

        elif escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4:
            opcao_escolhida(escolha)

        else:
            
            print("Digite uma opcao correta ")