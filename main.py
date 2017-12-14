#https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
#https://pythondigest.ru/view/17328/
#https://habrahabr.ru/post/280238/
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#pip install BS4
#pip install lxml

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

pdd_url = "http://www.avtoinstruktor76.ru/bileti_B/bileti_pdd_2017_on-lain_oficialni_tekst_GIBDD_kategoriya_B.php"
pdd_bilet_url = "http://www.avtoinstruktor76.ru/bileti_B/"

def startScraping():
    bileti_urls = []
    print("Start scraping...")
    try:
        html = urlopen(pdd_url)
    except HTTPError as e:
        html = None
        print(e)
        return
    else:
        try:
            bsObj = BeautifulSoup(html.read(),"html.parser")
        except Exception as e:
            print(e)
            return
        else:
            #print(bsObj.prettify())
            for link in bsObj.findAll("a"):
                linkhref = link.get('href')
                if linkhref.startswith("bileti") and linkhref.endswith(".php"):
                    bileti_urls.append(pdd_bilet_url+linkhref)
    if len(bileti_urls)==0:
        print("Can't find any bilty hrefs")
        return

    for url in bileti_urls:
        pass


def startStuding():
    print("start studing")



if __name__ == '__main__':
    print("What is your choice: scaping or studing?")
    value = input()
    if value.lower() in {'sc','scr','scrap','scraping'}:
        print("Wonna scraping, are you sure?")
        value = input()
        if value.lower() in {'y','yes','yep'}:
            startScraping()
        else:
            print("Cancelled!")
            value = input()
    elif value.lower() in ('st','study','studing'):
        startStuding()
    else:
        print("Does not know what you want!")
        value = input()
