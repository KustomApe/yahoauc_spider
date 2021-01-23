import requests
import urllib.request as urlreq
from bs4 import BeautifulSoup

def main():
    url_origin = 'https://auctions.yahoo.co.jp/'
    keywords = input()

    r = urlreq.Request(url)
    with urlreq.urlopen(r) as r:
        r = r.read()