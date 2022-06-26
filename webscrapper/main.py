from bs4 import BeautifulSoup

import requests

# Dizer de qual site vai ser pegada as informacoes
# pega todo codigo html
site = requests.get("https://www.climatempo.com.br/").content

# objeto site - recebe todo o conteudo da requisicao do site 

# O objeto soup baixa do site o html dele com o 'html.parser'
soup = BeautifulSoup(site, 'html.parser')

# O prettify transforma um html em string 
#print(soup.prettify)

# Um Web Scrapping é um programa de analise, dai a gente consegue trazer só as informacoes que a gente quer 

# coloco o target e a classe.
#<img alt="Altura máxima da onda" class="lazyload _margin-l-10 _margin-r-5"
# Observe que após o class tem um _ ficando class_
conteudo = soup.find("h3", class_="title -gray-dark-2 _margin-b-10")

# Pra transformar a estrutura html em string
print(conteudo.string)

print(soup.title)
print(soup.title.string)
print(soup.a.string)
print(soup.find('admin'))
