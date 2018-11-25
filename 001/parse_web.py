import requests
from bs4 import BeautifulSoup as bs
_url="https://pl.wikipedia.org/"
_r=requests.get(_url)
_text=_r.text
_parsed=bs(_text,features='html.parser')
_article=_parsed.find('div',id="main-page-good-article")
print(_article.text)