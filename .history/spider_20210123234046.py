import requests
import urllib.request as urlreq
from bs4 import BeautifulSoup

def main():
    url = 'https://auctions.yahoo.co.jp/'
    r = urlreq.Request(url)
    with urlreq.urlopen(r) as r:
        r = r.read()