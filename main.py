#https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
#https://pythondigest.ru/view/17328/
#https://habrahabr.ru/post/280238/



def startScrapping():
    print("start scrapping")


def startStuding():
    print("start studing")



if __name__ == '__main__':
    print("What is your choice: scapping or studing?")
    value = input()
    if value.lower() in {'sc','scr','scrap','scrapping','scrapping'}:
        print("Wonna scrapping, are you sure?")
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
