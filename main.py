#https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
#https://pythondigest.ru/view/17328/
#https://habrahabr.ru/post/280238/
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#pip install BS4
#pip install lxml
#pip install request

import const

from urllib.request import urlopen
from urllib.error import HTTPError
import urllib.parse
from bs4 import BeautifulSoup

from os import system, getcwd, makedirs, listdir, remove
from os.path import join, dirname, exists, splitext, isfile, getctime, split
import shutil
from datetime import datetime
from time import sleep
from requests import get

import json


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
            #removedirs(dirname)
        except Exception as e:
            pass
        finally:
            makedirs(dirname)
    bn = 0
    starttime = datetime.now()
    for url in bileti_urls:
        bn += 1
        if bn ==1010:
            continue
        try:
            html = urlopen(url)
        except HTTPError as e:
            html = None
            print("Can't open url "+url)
        else:
            print("Scraping "+url)
            try:
                bsObj = BeautifulSoup(html.read(),"html.parser")
            except Exception as e:
                print("Error while parsing "+url)
            else:
                try:
                    makedirs(join(dirname,const.bilet_dir_prefix+const.bilet_dir_format.format(bn)))
                    qs = bsObj.findAll('p',{'align':'center'},{'class':'стиль10'})
                    bnq = 0
                    for q in qs:
                        print('[{0}] {1:.0f}%'.format('#'*int((const.progress_size*bnq/len(qs))), 100*bnq/len(qs)),end='\r')
                        questionTitle = ""
                        questionImageUrl = ""
                        questionOptions = []
                        questionAnswer = 0
                        questionExplanation = ""
                        jd = {}
                        if q.get_text().startswith(const.bilet_ptext):
                            bnq += 1
                            qparent = q.parent.parent.parent
                            questionTitle=qparent.find('span',{'class':'стиль2'}).get_text().replace("\r","").replace("\n","").lstrip().rstrip()
                            q=qparent.find('img')
                            if q is not None:
                                questionImageUrl=q['src']
                            ops = qparent.findAll('span',{'class':'стиль4'})
                            for o in ops:
                                o1 = o.get_text().replace("\r","").replace("\n","")
                                i = o1.find('.')
                                questionOptions.append(o1[i+1:].lstrip().rstrip())
                            a=qparent.find('button')['title']
                            i=a.find("ответ:")
                            questionAnswer=int(a[len("ответ:")+i:len("ответ:")+i+2])
                            i=a.find("Комментарии:")
                            questionExplanation=a[len("Комментарии:")+i:].replace("\r","").replace("\n","").lstrip().rstrip()
                            jd["Title"]=questionTitle
                            if questionImageUrl:
                                imageURL = urllib.parse.urljoin(const.pdd_bilet_url, questionImageUrl)
                                path = urllib.parse.urlparse(imageURL).path
                                imageName = str(bnq)+splitext(path)[1]
                                with open(join(dirname,const.bilet_dir_prefix+const.bilet_dir_format.format(bn),imageName), "wb") as imgfile:
                                    response = get(imageURL)
                                    imgfile.write(response.content)
                                #urllib.request.urlretrieve(imageURL, join(dirname,const.bilet_dir_prefix+const.bilet_dir_format.format(bn),imageName))
                            else:
                                imageName=""
                            jd["ImageName"]=imageName
                            jd["Options"]=questionOptions
                            jd["Answer"]=questionAnswer
                            jd["Explanation"]=questionExplanation
                            with open(join(dirname,const.bilet_dir_prefix+const.bilet_dir_format.format(bn),'question'+str(bnq)),"x",encoding="utf-8") as f:
                            	json.dump(jd,f)
                            if const.question_sleep:
                                sleep(const.question_sleep)

                except Exception as e:
                    print("Ошибка: Билет:"+str(bn)+" Вопрос:"+str(bnq)+":"+str(e))
            if const.bilet_sleep:
                sleep(const.bilet_sleep)
            break
    print('\r------------------- Done in  {} -------------------'.format(datetime.now() - starttime))

def startStuding():
    print("start studing")


if __name__ == '__main__':
    print("What is your choice: scraping or studing?")
    value = input()
    if value.lower() in {'sc','scr','scrap','scraping'}:
        print("Wonna scraping, are you sure?")
        value = input()
        if value.lower() in {'y','yes','yep'}:
            startScraping()
        else:
            print("Cancelled!")
            value = input()
    elif value.lower() in {'st','study','studing'}:
        startStuding()
    else:
        print("Does not know what you want!")
        value = input()
