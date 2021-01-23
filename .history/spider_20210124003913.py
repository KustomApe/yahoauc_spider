import io,sys
import requests
import urllib.request as urlreq
import urllib.parse
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def main():
    words = input("検索したいキーワードを入力してください(複数の場合は半角スペースで区切ってください)：").split(' ')
    word = '+'.join(words)
    word_encoded = urllib.parse.quote(word.encode('utf-8'))
    url_origin = 'https://auctions.yahoo.co.jp/search/search?auccat=&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&exflg=1&p='
    url = url_origin + word_encoded
    print(url)
    r = urlreq.Request(url)
    with urlreq.urlopen(r) as r:
        r = r.read()
    soup = BeautifulSoup(r, 'html.parser')
    for post in posts:
        posts = soup.find_all('li', class_='Product')
        img = 
        name
        price_now
        price_close
        limit


if __name__ == '__main__':
    main()