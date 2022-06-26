import requests # trabalhar com http
from bs4 import BeautifulSoup # mexer com html e xml 
import operator # trabalhar com operadores 
from collections import Counter # ajuda a manipular estrutura de dados

# Esta funcao define todo o webcrawler 
# comeca na url 
def start(url):
    # Lista vazia pra armazenar todo o conteudo do site 
    wordlist = []
    
    
    source_code = requests.get(url).text
    print(source_code)

    # Faz a requisicao dos dados da url passado e transforma em html 
    soup = BeautifulSoup(source_code, 'html.parser')

    # Varre o codigo em soup e procura tudo relacionado ao conteudo dentro de soup.findAll()
    # E transforma o codigo html em texto
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        
        # Transforma em texto um conteudo
        content = each_text.text
        
        # transforma em letras minusculas e corta o conteudo sendo cada um deles uma linha diferente
        words=content.lower().split()

        for each_word in words:
            wordlist.append(each_word)

        # Remove qualquer simbolo indesejado da wordlist
        clean_wordlist(wordlist)

###################
# Remover caracteres especiais de wordlist, criando uma clean_list:

def clean_wordlist(wordlist):

    clean_list = []
    symbols = '!@#$%&*()+-+=[]{}|\"/,.;:?<> '
    symbols += '–…'

    # Para cada palavra dentro da wordlist
    for word in wordlist:
        print(f'A palavra na wordlist: {word}')
        # Que contenha os simbolos

        for i in range(0, len(symbols)):
            # Na palavra, aonde tiver um caracter de symbols[i] vc troca por vazio ''
                word = word.replace(symbols[i], '')

                if len(word) > 0:
                    clean_list.append(word)
        create_dictionary(clean_list)

def create_dictionary(clean_list):
        word_count = {}

        for word in clean_list:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        # key=operator.itemgetter(1) - pega o primerio item
        for key,value in sorted(word_count.items(), key=operator.itemgetter(1)):
            print(f'{key} : {value}')

        print('#'*40)
        c = Counter(word_count)
        top = c.most_common(10)
        print(top)
        print('#'*40)
        print(word_count)


if __name__ == "__main__":
    print('#'*40)

    url = 'https://www.geeksforgeeks.org/machine-learning/'
    start(url)
