import requests
from bs4 import BeautifulSoup as bs

def getArticle():
    """
    Pobierz wyróżniony artykuł z Wikipedii.
    Zwróć artykuł jako tekst.
    """
    _url="https://pl.wikipedia.org/"
    _r=requests.get(_url)
    _text=_r.text
    _parsed=bs(_text,features='html.parser')
    _article=_parsed.find('div',id="main-page-good-article")
    return(_article.text)


if __name__=="__main__":
    print(getArticle())