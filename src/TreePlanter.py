from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

driver = webdriver.Chrome('D:\Development\chromedriver\chromedriver.exe')

driver.get('https://relatedwords.org/relatedto/sustainability')

links = driver.find_elements(By.XPATH,"//a[@class='item']")

keywords = []

for link in links:
    keywords.append(link.text)

print(keywords)
base_url = 'https://www.ecosia.org/'

while True:
    driver.get(base_url)

    searchbox = driver.find_element(By.XPATH,"//*[@class='search-form__input']")
    searchbox.send_keys(random.choice(keywords))
    searchbox.send_keys(Keys.ENTER)
    sublinks=[]
    while len(sublinks) == 0 :
        sublinks = driver.find_elements(By.XPATH , "//a")
        print(len(sublinks))
        time.sleep(2)
    recheck = True
    while recheck:
        try:
            sub_sub_set = []
            if len(sublinks) > 7:
                sub_sub_set = sublinks[7::]
            else:
                sub_sub_set = sublinks
            active_link = random.choice(sub_sub_set)
            print(active_link)
            active_link.click()
            time.sleep(random.randint(5,15))
            recheck = False
        except:
            print(f'Active link failed retrying')
            time.sleep(1)





