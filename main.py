#https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
#https://pythondigest.ru/view/17328/
#https://habrahabr.ru/post/280238/


pdd_url = "http://www.avtoinstruktor76.ru/bileti_B/bileti_pdd_2017_on-lain_oficialni_tekst_GIBDD_kategoriya_B.php"

def startScraping():

    print("start scraping")


def startStuding():
    print("start studing")



if __name__ == '__main__':
    print("What is your choice: scaping or studing?")
    value = input()
    if value.lower() in {'sc','scr','scrap','scraping'}:
        print("Wonna scraping, are you sure?")
        value = input()
        if value.lower() in {'y','yes','yep'}:
            startScrapping()
        else:
            print("Cancelled!")
            value = input()
    elif value.lower() in ('st','study','studing'):
        startStuding()
    else:
            print("Does not know that you want!")
            value = input()
