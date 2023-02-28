from bs4 import BeautifulSoup
from lxml import etree
import subprocess
import os



def access():
    
    try:
        scrapethis = os.path.realpath("output2.html")
        print(scrapethis)
    except:
        print('err')
        pass

    with open(scrapethis, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser", from_encoding="utf-8")
        dom = etree.HTML(str(soup))
        print('meme')
        
        x = 0
        
        #macroelemnt = class="css-53u6y8"
        
        
        try:
            while x < 200:
                tac = (dom.xpath('//p[@class="css-at9mc1 evys1bk0"]')[x].text)
                if tac != None:
                    print(tac)
                    print("\n")
                else:
                    pass
                x+=1
        except:
            pass
    
access()
