import urllib.request

c = (
    '\033[m',      # limpa
    '\033[0;32m',  # verde
    '\033[0;31m'   # vermelho
)

try:
    url = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print(f'{c[2]}O site Pudim não está acessível no momento.{c[0]}')
else:
    print(f'{c[1]}Conseguir acessar o site Pudim com sucesso!{c[0]}')
