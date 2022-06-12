#-------------IMPORTS-----------------
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from requests.sessions import session
from tomlkit import comment
#-------------CONFIGSITE-----------------
session = requests.Session()
session.headers['User-Agent']
'python-requests/2.19.1'
my_headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.214',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
#-------------LISTA-----------------
lista_imoveis =[]
#-------------INSERE SITE-----------------
#url = input('digite o site: ')
url = 'https://sp.olx.com.br/sao-paulo-e-regiao/zona-sul/saude/imoveis/venda/casas?o=2&roe=4&ros=2&se=8&ss=4'
response = requests.get(url, headers=my_headers)
#-------------CODIGO-----------------
site = BeautifulSoup(response.text, "html5lib")
imoveis = site.findAll('li', class_= 'sc-1fcmfeb-2 juiJqh')
print(imoveis)
#for imovel in imoveis:
#    titulo = imovel.find('h2', class_='sc-1mbetcw-0 fKteoJ sc-ifAKCX jyXVpA').getText()
#    valor = imovel.findAll('span', class_='sc-ifAKCX eoKYee')[0].contents[0]
#    valor = float(valor.replace('.',''))
#    valor = valor.split('R$')[1]
#    link = imovel.find('a')['href']
#    dados = imovel.findAll('span', class_ ='sc-1j5op1p-0 lnqdIU sc-ifAKCX eLPYJb')[0].contents[0]
#    dados = dados.strip()
#    quarto = dados.split('|')[0].strip()
#    quarto = quarto.replace('quartos','')
#    quarto = quarto.replace('quarto','')
#    quarto = quarto.replace('ou mais','')
#    metro = dados.strip()
#    metro = metro.split('|')[1].strip()
#    metro = metro.replace('m²','')
#    condo = dados.strip()
#    condo = condo.split('|')[2].strip()
#    condo = condo.replace('Condomínio: ','')
#    condo = condo.replace('.','')
#    condo = condo.replace(',','')
#    condo = float(condo.replace('R$',''))
#    vagas = dados.strip()
#    vagas = vagas.split('|')[3].strip()
#    vagas = vagas.replace('vagas','')
#    vagas = vagas.replace('vaga','')
#    vagas = vagas.replace('vagas','')
#    vagas = vagas.replace('ou mais','')
#    local = imovel.findAll('span', class_='sc-7l84qu-1 ciykCV sc-ifAKCX dpURtf')[0].contents[0]
#    local = local.strip()
#    local = local.split(',')[1].strip()
#    lista_imoveis.append([local,valor,metro,quarto,vagas,condo,titulo,link])
#print(lista_imoveis)
