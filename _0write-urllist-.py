import time
from datetime import datetime


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import pandas as pd
import xlwt

import xlwt
from xlwt import Workbook

import subprocess

import random
import os


wb = Workbook()

subprocess.call("test.bat")

sheet1 = wb.add_sheet('Sheet 1')

f = open('urllist','w')

def access():
    
    try:
        scrapethis = os.path.realpath("output2.html")
        print(scrapethis)
    except:
        print('err')
        pass


    # -
    # - 
    #
        
    
    
    chrome_options = Options() 
    
    chrome_options.add_argument('--user-data-dir=H:/Projects/NYTRIP/User Data')
    chrome_options.add_argument('--profile-directory=Profile 3')
    
    driver = webdriver.Chrome()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-dev-shm-usag')
    
    #Gets rid of errors \ selenium hook log bs
    
    #Makes it go Slightly faster, I think


    #Makes it go Slightly faster, I think
    
    
     
    #Search Filter
    query = "immigration"
    end_date = "20230220" #Year | #Month | #Day 
    #End Date
    start_date = "20220920" #Year | #Month | #Day
    site_access = ("https://www.nytimes.com/search?dropmab=false&endDate={}&query={}&sort=oldest&startDate={}".format(end_date, query, start_date))
    
    print(site_access)
    driver.get(site_access)
    time.sleep(2)
    
    veri = 1
    s = 0
    article_grab = 0
    
    spreadsheetcont = 0
    while veri == 1:
        try:
            driver.find_element(By.XPATH, '//*[@data-testid="search-show-more-button"]').click() 
            
            try:
                
                for i in range(10):
                    article_grab+=1
                    url = (driver.find_elements(By.XPATH, '//*[@class="css-e1lvw9"]//a')[article_grab].get_attribute('href'))
                    print(url)
                    f.write(url + '\n')
                    sheet1.write(spreadsheetcont, 0, url)
                    spreadsheetcont+=1
            except:
                pass
            time.sleep(.5)
        except:
            s+=1
            print(s)
            if s> 1000:
                break
            else:
                pass
    
    print('terminate')

access()
wb.save('xlwt example.xls')
f.close()

exec(open('_1create-outsidehtml.py').read())
