## Boiler Plate code for running proxies with beautiful soup
import random, requests
from bs4 import BeautifulSoup
from proxy import *
PROXIES_LIST_ = []

def make_soup(url, retry):
    global proxy_string
    for row in proxy_string.split():
        if row:
            PROXIES_LIST_.append(row.strip())
            pass

    print(PROXIES_LIST_)

    proxyDict = {
              "http"  : random.choice(PROXIES_LIST_),
              "https" : random.choice(PROXIES_LIST_),
              "ftp"   : random.choice(PROXIES_LIST_)
            }
    try:
        html = requests.get(url, headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}, proxies=proxyDict).content
    except:
        print("Fail to request " + url + " with proxy: " + str(proxyDict['https']))
        if retry < 0:
            return None
        else:
            return make_soup(url, retry-1)
    return BeautifulSoup(html, "html.parser")


def walmart():
    url = ["https://www.walmart.com/ip/Ripple-Plant-Based-Protein-Powder-Vanilla-20g-Protein-14-3oz/693580252"]
    for i in range(len(url)):
        try:
            print('WALMART Index ' + str(i) + ' in URLs is: ' + url[i])
            soup = make_soup(url[i], 5)
            print(soup)
        except:
            print("Error")


walmart()
