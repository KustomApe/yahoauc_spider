import io,sys
import requests
import urllib.request as urlreq
import urllib.parse
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# def main():
words = input("検索したいキーワードを入力してください(複数の場合は半角スペースで区切ってください)：").split(' ')
word_encoded = urllib.parse.quote(words)
word = '+'.join(words)
print(word)
url_origin = 'https://auctions.yahoo.co.jp/search/search?auccat=&tab_ex=commerce&ei=utf-8&aq=-1&oq=&sc_i=&exflg=1&p='
url1 = url_origin + word
r = urlreq.Request(url)
with urlreq.urlopen(r) as r:
    r = r.read()
soup = BeautifulSoup(r, 'html.parser')
posts = soup.find_all('li', class_='Product')
child = posts.findChild('img', recursive=False)
for post in posts:
    print(post)


if __name__ == '__main__':
    main()