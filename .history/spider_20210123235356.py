# -*- coding: utf-8 -*-

import requests
import urllib.request as urlreq
from bs4 import BeautifulSoup

# def main():
words = input("検索したいキーワード1つ目を入力してください：").split(',')
for i in words:
    
print(word)
url_origin = 'https://auctions.yahoo.co.jp/search/search?auccat=&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&exflg=1&p='
url = url_origin + word
print(url)