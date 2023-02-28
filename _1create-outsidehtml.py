import time
import os
import subprocess
from bs4 import BeautifulSoup
from lxml import etree


    


with open('urllist') as topo_file:
    for line in topo_file:
        #print(line) 
        #command_string = str('H://Projects//NYTRIP//curl-7.88.1_1-win64-mingw//bin//curl.exe ' + line + ' > output1.html')
        #time.sleep(1)
        #subprocess.run(command_string, shell=True)
        
        newl = line.replace('https://www.nytimes.com/', '')
        
        anewl = newl.replace('/', '')
        
        bnewl = anewl.replace(".html?searchResultPosition", "")
        
        cnewl = bnewl.replace('=', '')
        cnewl = cnewl.strip()
        
        urlstr = str(cnewl + '.txt')
                
        command_string_2 = ('py H://Projects//NYTRIP//_2_rip-text.py > {}').format(urlstr)

        print(command_string_2)
        subprocess.run(command_string_2, shell=True)
        
        
         
        
         
        

        
        