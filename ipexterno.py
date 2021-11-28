import re, json
from urllib.request import urlopen

'''
Este aplicativo oferece informações sobre o ip do usuário...

'''

url = f'https://ipinfo.io/json'

response = urlopen(url)

data = json.load(response)

ip = data['ip']
org = data['org']
cid = data['city']
pais = data['country']
regiao = data['region']

print('Detalhes do IP externo: \n')
print(f'IP: {ip}\nOrgão: {org}\nCidade: {cid}\nRegião: {regiao}\nPaís: {pais}...')