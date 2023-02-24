import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import subprocess

import random
import os

subprocess.call("test.bat")

def access():
    
    try:
        scrapethis = os.path.realpath("output.html")
        print(scrapethis)
    except:
        print('err')
        pass
        
        
    
    
    chrome_options = Options() 
    
    chrome_options.add_argument('--user-data-dir=H:/Projects/NYTRIP/User Data')
    chrome_options.add_argument('--profile-directory=Profile 3')
    #chrome_options.add_argument()
    
    driver = webdriver.Chrome(chrome_options=chrome_options)
    
    
    #Gets rid of errors \ selenium hook log bs
    chrome_options.add_argument('--log-level=3')
    
    #Gets rid of errors \ selenium hook log bs
    
    #Makes it go Slightly faster, I think

    
    #Makes it go Slightly faster, I think
    
    
    
    #Search Filter
    query = "wipty"
    end_date = "20230220" #Year | #Month | #Day 
    #End Date
    start_date = "20120220" #Year | #Month | #Day
    #site_access = ("https://www.nytimes.com/search?dropmab=false&endDate={}&query={}&sort=oldest&startDate={}".format(end_date, query, start_date))
    
    site_access = (scrapethis)
    
    print(site_access)
        
    driver.get(site_access)
    
    
    
    x = 0
    val1 = driver.find_element_by_xpath('//*[@class="css-at9mc1 evys1bk0"]')[1].get_attribute("innerText")
    print(val1)
    
   #]\//*[@class="css-at9mc1 evys1bk0"]

    #driver.get(site_access)
    #print('We are on ' + site_access)
    #time.sleep(2)


access()

#Rip bodies of text