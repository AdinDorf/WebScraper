from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.theonion.com/")
bsObj = BeautifulSoup(html.read())

article_containers = bsObj.find_all('div','curation-module__item__wrapper')
for n in article_containers:
    soup_string = str(article_containers[n].find_all('div','content-meta__headline__wrapper'))
    try:
        hl_indexstart = soup_string.index("https:")
           #find end of hyperlink
        hl_indextemp = soup_string[hl_indexstart:]
        hl_indexend = hl_indextemp.index('" ')
        hl_link = hl_indextemp[:hl_indexend]
        print(hl_link)

        try:
            htmlinner = urlopen(hl_link)
            innerbsObj = BeautifulSoup(htmlinner.read())
            article_string = str(innerbsObj.p)
            print(article_string)
            f = open('onion.txt','w')
            f.write(article_string + "~~\n")
            f.close()
        except:
            print("could not open link")
    except:
        print("no hyperlink found")

    

 