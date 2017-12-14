#https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
#https://pythondigest.ru/view/17328/
#https://habrahabr.ru/post/280238/
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#pip install BS4
#pip install lxml

import const

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

from os import system, getcwd, makedirs, listdir, remove
from os.path import join, dirname, exists, splitext, isfile, getctime, split
import shutil
from datetime import datetime

def startScraping():
    bileti_urls = []
    print("Start scraping...")
    try:
        html = urlopen(const.pdd_url)
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
                    bileti_urls.append(const.pdd_bilet_url+linkhref)
    if len(bileti_urls)==0:
        print("Can't find any hrefs")
        return
    else:
        dirname = join(getcwd(), const.data_dir)
        try:
            shutil.rmtree(dirname)
            removedirs(dirname)
        except Exception as e:
            pass
        finally:
            makedirs(dirname)
    bn = 0
    starttime = datetime.now()
    for url in bileti_urls:
        bn += 1
        try:
            html = urlopen(url)
        except HTTPError as e:
            html = None
            print("Can't open url "+url)
        else:
            print("Scaping "+url)
            try:
                bsObj = BeautifulSoup(html.read(),"html.parser")
            except Exception as e:
                print("Error while parsing "+url)
            else:
                makedirs(join(dirname,const.bilet_dir_prefix+const.bilet_dir_format.format(bn)))
    print('Done in  {}'.format(datetime.now() - starttime))



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
