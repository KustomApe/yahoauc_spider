import requests
import urllib.request as urlreq
from bs4 import BeautifulSoup

# def main():
word = input("検索したいキーワード1つ目を入力してください：")
url_origin = 'https://auctions.yahoo.co.jp/search/search?auccat=&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&exflg=1&p='
keywords = keyword + '&x=0&y=0'
url = url_origin + keywords
r = urlreq.Request(url)
with urlreq.urlopen(r) as r:
    r = r.read()
soup = BeautifulSoup(r, 'html.parser')