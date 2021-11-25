from bs4 import BeautifulSoup
import requests


site = requests.get("https://www.remessaonline.com.br/cotacao/cotacao-dolar").content

soup = BeautifulSoup(site, 'html.parser')

# prettify transforma o html em string
print(soup.prettify())

Dolar = soup.find("div", class_="style__Text-sc-15flwue-2 cSuXFv")
title = soup.title
# print(title.string) 
print(f'Valor do Dolar comercial hoje: R$ {(Dolar.string).replace(" Reais", "...")}')
