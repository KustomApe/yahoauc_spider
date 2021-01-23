import requests
import urllib.request as urlreq
from bs4 import BeautifulSoup

def main():
    url_origin = 'https://auctions.yahoo.co.jp/search/search?auccat=&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&exflg=1&p='
    keywords = input()
    keywords_final = keywords + '&x=0&y=0'

    r = urlreq.Request(url)
    with urlreq.urlopen(r) as r:
        r = r.read()