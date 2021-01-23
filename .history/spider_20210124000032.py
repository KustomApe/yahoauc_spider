# -*- coding: utf-8 -*-

import requests
import urllib.request as urlreq
from bs4 import BeautifulSoup

def main():
    words = input("検索したいキーワードを入力してください(複数の場合は半角スペースで区切ってください)：").split(' ')
    print(words)
    word = '+'.join(words)
    print(word)
    url_origin = 'https://auctions.yahoo.co.jp/search/search?auccat=&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&exflg=1&p='
    url = url_origin + word
    r = urlreq.Request(url)
    with urlreq.urlopen(r) as r:
        r = r.read()
